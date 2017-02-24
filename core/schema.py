import types

import graphene
import requests
from graphene import resolve_only_args

from schemas.encounter import Encounter
from schemas.encounter_provider import EncounterProvider
from schemas.obs import Obs
from schemas.patient import Patient
from schemas.patient_identifier import PatientIdentifier
from schemas.person import Person
from schemas.person_address import PersonAddress
from schemas.person_attribute import PersonAttribute
from schemas.person_name import PersonName
from schemas.visit import Visit
from database import Database

db = Database()


class Attribute(graphene.InputObjectType):
    t = graphene.String(required=True)
    v = graphene.String(required=True)


class Query(graphene.ObjectType):
    obs = graphene.List(Obs, )
    encounters = graphene.List(Encounter, )
    encounter_providers = graphene.List(EncounterProvider, )
    persons = graphene.List(Person, offset=graphene.Int(), limit=graphene.Int())
    patients = graphene.List(Patient, )
    person_names = graphene.List(PersonName, )
    person_attributes = graphene.List(PersonAttribute, )
    patient_identifiers = graphene.List(PatientIdentifier, )
    visits = graphene.List(Visit, )
    person_addresses = graphene.List(PersonAddress, )
    patient = graphene.Field(Patient, attribute=Attribute())

    @resolve_only_args
    def resolve_obs(self):
        data = db.query("select * from obs")
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

    @resolve_only_args
    def resolve_persons(self, offset=None, limit=None):
        if offset and limit:
            data = db.query("select * from person LIMIT " + str(offset) + ", " + str(limit))
        else:
            data = db.query("select * from person")

        all_data = [Person(**d) for d in data]
        return all_data

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
    def resolve_patient(self, attribute=None):
        data = None
        if attribute:
            attribute_type = attribute.get('t')
            if attribute_type == 'a41339f9-5014-45f4-91d6-bab84c6c62f1':
                r = requests.post('http://localhost:8080/fingerprint/', data={'fingerprint': attribute.get('v')})
                patient = r.json()

                if patient.get('person') != 'null':
                    data = db.query_one("select * from patient where uuid='" + patient.get('person'))
            else:
                data = db.query_one(
                    "select * from patient where uuid in (select person from person_attribute where person_attribute_type ='" + attribute_type + "' and value ='" + attribute.get('v') + "')")
        if data:
            all_data = Patient(**data)
            return all_data
        return None


schema = graphene.Schema(query=Query)
