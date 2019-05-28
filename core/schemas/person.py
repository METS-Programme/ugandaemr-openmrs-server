import graphene

from core.database import Database
import encounter
import obs
import patient_identifier
import person_address
import person_attribute
import person_name
import visit

db = Database()


class Person(graphene.ObjectType):
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

    addresses = graphene.List(person_address.PersonAddress, )
    attributes = graphene.List(person_attribute.PersonAttribute, )
    names = graphene.List(person_name.PersonName, )
    identifiers = graphene.List(patient_identifier.PatientIdentifier, )
    encounters = graphene.List(encounter.Encounter, )
    obs = graphene.List(obs.Obs, )
    visits = graphene.List(visit.Visit, )

    def resolve_addresses(self, args, *_):
        data = db.query("select * from person_address where person = '" + self.uuid + "'")
        all_data = [person_address.PersonAddress(**d) for d in data]
        return all_data

    def resolve_attributes(self, args, *_):
        data = db.query("select * from person_attribute where person = '" + self.uuid + "'")
        all_data = [person_attribute.PersonAttribute(**d) for d in data]
        return all_data

    def resolve_names(self, args, *_):
        data = db.query("select * from person_name where person = '" + self.uuid + "'")
        all_data = [person_name.PersonName(**d) for d in data]
        return all_data

    def resolve_identifiers(self, args, *_):
        data = db.query("select * from patient_identifier where patient = '" + self.uuid + "'")
        all_data = [patient_identifier.PatientIdentifier(**d) for d in data]
        return all_data

    def resolve_encounters(self, args, *_):
        data = db.query("select * from encounter where patient = '" + self.uuid + "'")
        all_data = [encounter.Encounter(**d) for d in data]
        return all_data

    def resolve_obs(self, args, *_):
        data = db.query("select * from obs where person = '" + self.uuid + "'")
        all_data = [obs.Obs(**d) for d in data]
        return all_data

    def resolve_obs(self, args, *_):
        data = db.query("select * from visit where patient = '" + self.uuid + "'")
        all_data = [obs.Obs(**d) for d in data]
        return all_data
