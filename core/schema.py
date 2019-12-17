import types

import graphene
import requests
from graphene import resolve_only_args

from core.schemas.facility import Facility
from core.schemas.transfered_patient import TransferedPatient
from core.schemas.encounter import Encounter
from core.schemas.encounter_provider import EncounterProvider
from core.schemas.obs import Obs
from core.schemas.patient import Patient
from core.schemas.patient_identifier import PatientIdentifier
from core.schemas.person_address import PersonAddress
from core.schemas.person_attribute import PersonAttribute
from core.schemas.person_name import PersonName
from core.schemas.visit import Visit
from core.database import Database

db = Database()


class Attribute(graphene.InputObjectType):
    t = graphene.String(required=True)
    v = graphene.String(required=True)


class Identifier(graphene.InputObjectType):
    t = graphene.String(required=True)
    v = graphene.String(required=True)


class Query(graphene.ObjectType):
    obs = graphene.List(Obs, )
    encounters = graphene.List(Encounter, )
    encounter_providers = graphene.List(EncounterProvider, )
    # persons = graphene.List(Person, offset=graphene.Int(), limit=graphene.Int())
    patients = graphene.List(Patient, )
    person_names = graphene.List(PersonName, )
    person_attributes = graphene.List(PersonAttribute, )
    patient_identifiers = graphene.List(PatientIdentifier, )
    visits = graphene.List(Visit, )
    person_addresses = graphene.List(PersonAddress, )
    patient = graphene.Field(Patient, patient=graphene.String(), identifier=Identifier(), attribute=Attribute(),
                             patients=graphene.List(graphene.String))
    patient_obs = graphene.List(Obs, patientuuid=graphene.String(), conceptsuuid=graphene.List(graphene.String))
    facilities = graphene.List(Facility, )
    transfered_patient = graphene.List(TransferedPatient, transfer_out_from=graphene.String())

    @resolve_only_args
    def resolve_obs(self):
        data = db.query(
            "select o.*,e.encounter_datetime as encounter_date,e.encounter_type as encounter_type from obs o inner join encounter e on(o.encounter = e.uuid)")
        all_data = [Obs(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_encounters(self):
        data = db.query("select * from encounter")

        all_data = [Encounter(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_encounter_providers(self):
        data = db.query("select * from encounter_provider")
        all_data = [EncounterProvider(**d) for d in data]
        return all_data

    # @resolve_only_args
    # def resolve_persons(self, offset=None, limit=None):
    #     if offset and limit:
    #         data = db.query("select * from person LIMIT " + str(offset) + ", " + str(limit))
    #     else:
    #         data = db.query("select * from person")
    #
    #     all_data = [Person(**d) for d in data]
    #     return all_data

    @resolve_only_args
    def resolve_patients(self):
        data = db.query("select * from patient")
        all_data = [Patient(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person_names(self):
        data = db.query("select * from person_name")
        all_data = [PersonName(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person_attributes(self):
        data = db.query("select * from person_attribute")
        all_data = [PersonAttribute(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_patient_identifiers(self):
        data = db.query("select * from patient_identifier")
        all_data = [PatientIdentifier(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_visits(self):
        data = db.query("select * from visit")
        all_data = [Visit(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person_addresses(self):
        data = db.query("select * from person_address")
        all_data = [PersonAddress(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_patient(self, patient=None, identifier=None, attribute=None, patients=None):
        data = None

        if patient is not None:
            data = db.query_one("select * from patient where uuid ='" + patient + "'")
        elif patients is not None:
            q = ','.join(map("'{0}'".format, patients))
            data = db.query_one("select * from patient where uuid in(" + q + ")")
        elif identifier is not None:
            identifier_type = identifier.get('t')
            data = db.query_one(
                "select * from patient where uuid in (select patient from patient_identifier where identifier_type ='" + identifier_type + "' and identifier ='" + identifier.get(
                    'v') + "')")

        elif attribute is not None:
            attribute_type = attribute.get('t')
            data = db.query_one(
                "select * from patient where uuid in (select person from person_attribute where person_attribute_type ='" + attribute_type + "' and value ='" + attribute.get(
                    'v') + "')")
        if data:
            all_data = Patient(**data)
            return all_data

        return None

    @resolve_only_args
    def resolve_patient_obs(self, patientuuid=None, conceptsuuid=None):
        data = None

        if patientuuid is not None and (conceptsuuid is not None or conceptsuuid is not None):
            concepts = ','.join(map("'{0}'".format, conceptsuuid))
            data = db.query("select * from obs where person ='" + patientuuid + "' and concept in(" + concepts + ")")
        if data:
            all_data = [Obs(**d) for d in data]
            return all_data

        return None

    @resolve_only_args
    def resolve_facilities(self):
        data = db.query("select * from facility")
        all_data = [Facility(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_transfered_patient(self, transfer_out_from=None):
        data = None
        if transfer_out_from is not None:
            data = db.query("select * from transfered_patient where transfered_out ='false' and transfered_out_from = '" + transfer_out_from +"'")
            all_data = [TransferedPatient(**d) for d in data]
            return all_data
        if data:
            all_data = [TransferedPatient(**d) for d in data]
            return all_data
        return None


schema = graphene.Schema(query=Query)
