import graphene
from graphene import resolve_only_args

from core.database import Database
from core.schemas.encounter import Encounter
from core.schemas.facility import Facility
from core.schemas.obs import Obs
from core.schemas.patient_identifier import PatientIdentifier
from core.schemas.person_address import PersonAddress
from core.schemas.person_attribute import PersonAttribute
from core.schemas.person_name import PersonName

db = Database()


class Patient(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()
    gender = graphene.String()
    birthdate = graphene.String()
    birthdate_estimated = graphene.String()
    dead = graphene.String()
    death_date = graphene.String()

    cause_of_death = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()
    changed_by = graphene.String()
    date_changed = graphene.String()

    voided = graphene.String()
    voided_by = graphene.String()
    date_voided = graphene.String()
    void_reason = graphene.String()
    uuid = graphene.String()

    facility = graphene.String()
    state = graphene.String()
    deathdate_estimated = graphene.String()
    birthtime = graphene.String()
    allergy_status = graphene.String()

    addresses = graphene.List(PersonAddress, )
    attributes = graphene.List(PersonAttribute, )
    names = graphene.List(PersonName, )
    identifiers = graphene.List(PatientIdentifier, )
    encounters = graphene.List(Encounter, types=graphene.List(graphene.String))
    obs = graphene.List(Obs, encounters=graphene.String())
    most_recent_encounter = graphene.Field(Encounter)
    most_recent_hiv_encounter = graphene.Field(Encounter)
    summary_page = graphene.Field(Encounter)
    patient_facility = graphene.Field(Facility, )

    def resolve_addresses(self, args, *_):
        data = db.query("select * from person_address where person = '" + self.uuid + "'")
        all_data = [PersonAddress(**d) for d in data]
        return all_data

    def resolve_attributes(self, args, *_):
        data = db.query("select * from person_attribute where person = '" + self.uuid + "'")
        all_data = [PersonAttribute(**d) for d in data]
        return all_data

    def resolve_names(self, args, *_):
        data = db.query("select * from person_name where person = '" + self.uuid + "'")
        all_data = [PersonName(**d) for d in data]
        return all_data

    def resolve_identifiers(self, args, *_):
        data = db.query("select * from patient_identifier where patient = '" + self.uuid + "'")
        print ("select * from patient_identifier where patient = '" + self.uuid + "'")
        all_data = [PatientIdentifier(**d) for d in data]
        return all_data

    def resolve_encounters(self, args, *_):
        data = db.query("select * from encounter where patient = '" + self.uuid + "'")
        all_data = [Encounter(**d) for d in data]
        return all_data

    def resolve_obs(self, args, *_):
        data = db.query("select * from obs where person = '" + self.uuid + "' LIMIT 5")
        all_data = [Obs(**d) for d in data]
        return all_data

    def resolve_patient_facility(self, args, *_):
        data = db.query_one("select * from facility where uuid ='" + self.facility + "'")
        all_data = Facility(**data)
        return all_data

    def resolve_most_recent_encounter(self, args, *_):
        data = db.query_one(
            "select * from encounter where uuid=(select uuid from (select uuid,MAX(encounter_datetime) from encounter where patient='" + self.uuid + "') A)")
        all_data = Encounter(**data)
        return all_data

    def resolve_most_recent_hiv_encounter(self, args, *_):
        data = db.query_one(
            "select * from encounter where uuid=(select uuid from (select uuid,MAX(encounter_datetime) from encounter where patient='" + self.uuid + "' and encounter_type = '8d5b2be0-c2cc-11de-8d13-0010c6dffd0f') A)")
        all_data = Encounter(**data)
        return all_data

    def resolve_summary_page(self, args, *_):
        data = db.query_one(
            "select * from encounter where uuid=(select uuid from (select uuid,MAX(encounter_datetime) from encounter where patient='" + self.uuid + "' and encounter_type = '8d5b27bc-c2cc-11de-8d13-0010c6dffd0f') A)")
        all_data = Encounter(**data)
        return all_data
