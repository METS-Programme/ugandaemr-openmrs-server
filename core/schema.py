import graphene
from graphene import relay
from graphene import resolve_only_args
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database import Database

db = Database()


class Encounter(graphene.ObjectType):
    id = graphene.ID()

    encounter_type = graphene.String()
    patient = graphene.String()
    location = graphene.String()
    form = graphene.String()
    encounter_datetime = graphene.String()

    creator = graphene.String()
    date_created = graphene.String()
    voided = graphene.String()
    voided_by = graphene.String()
    date_voided = graphene.String()

    void_reason = graphene.String()
    changed_by = graphene.String()
    date_changed = graphene.String()
    visit = graphene.String()
    uuid = graphene.String()

    facility = graphene.String()
    state = graphene.String()


class Obs(graphene.ObjectType):
    id = graphene.ID()
    person = graphene.String()
    concept = graphene.String()
    encounter = graphene.String()
    encounter_object = graphene.Field(Encounter)
    order = graphene.String()
    obs_datetime = graphene.String()

    location = graphene.String()
    obs_group = graphene.String()
    accession_number = graphene.String()
    value_group = graphene.String()

    value_boolean = graphene.String()
    value_coded = graphene.String()
    value_coded_name = graphene.String()
    value_drug = graphene.String()

    value_datetime = graphene.String()
    value_numeric = graphene.String()
    value_modifier = graphene.String()
    value_text = graphene.String()

    value_complex = graphene.String()
    comments = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()
    voided = graphene.String()

    voided_by = graphene.String()
    date_voided = graphene.String()
    void_reason = graphene.String()
    uuid = graphene.String()
    facility = graphene.String()

    state = graphene.String()
    previous_version = graphene.String()

    def resolve_encounter_object(self, args, *_):
        data = db.query_one("select * from encounter where uuid = '" + self.encounter + "'")
        return Encounter(**data)


class EncounterProvider(graphene.ObjectType):
    id = graphene.ID()
    encounter = graphene.String()
    provider = graphene.String()
    encounter_role = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()

    uuid = graphene.String()


class Person(graphene.ObjectType):
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


class Patient(graphene.ObjectType):
    id = graphene.ID()

    patient = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()
    changed_by = graphene.String()
    date_changed = graphene.String()

    voided = graphene.String()
    voided_by = graphene.String()
    date_voided = graphene.String()
    void_reason = graphene.String()
    allergy_status = graphene.String()

    facility = graphene.String()
    state = graphene.String()


class PersonName(graphene.ObjectType):
    id = graphene.ID()

    preferred = graphene.String()
    person = graphene.String()
    prefix = graphene.String()
    given_name = graphene.String()
    middle_name = graphene.String()

    family_name_prefix = graphene.String()
    family_name = graphene.String()
    family_name2 = graphene.String()
    family_name_suffix = graphene.String()

    degree = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()
    voided = graphene.String()
    voided_by = graphene.String()

    date_voided = graphene.String()
    void_reason = graphene.String()
    changed_by = graphene.String()
    date_changed = graphene.String()
    uuid = graphene.String()

    facility = graphene.String()
    state = graphene.String()


class PersonAttribute(graphene.ObjectType):
    id = graphene.ID()

    person = graphene.String()
    value = graphene.String()
    person_attribute_type = graphene.String()
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


class PatientIdentifier(graphene.ObjectType):
    id = graphene.ID()

    patient = graphene.String()
    identifier = graphene.String()
    identifier_type = graphene.String()
    preferred = graphene.String()
    location = graphene.String()

    creator = graphene.String()
    date_created = graphene.String()
    date_changed = graphene.String()
    changed_by = graphene.String()
    voided = graphene.String()

    voided_by = graphene.String()
    date_voided = graphene.String()
    void_reason = graphene.String()
    uuid = graphene.String()
    facility = graphene.String()

    state = graphene.String()


class Visit(graphene.ObjectType):
    id = graphene.ID()

    patient = graphene.String()
    visit_type = graphene.String()
    date_started = graphene.String()
    date_stopped = graphene.String()

    indication_concept = graphene.String()
    location = graphene.String()
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


class PersonAddress(graphene.ObjectType):
    id = graphene.ID()

    person = graphene.String()
    preferred = graphene.String()
    address1 = graphene.String()
    address2 = graphene.String()
    city_village = graphene.String()

    state_province = graphene.String()
    postal_code = graphene.String()
    country = graphene.String()
    latitude = graphene.String()
    longitude = graphene.String()

    start_date = graphene.String()
    end_date = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()
    voided = graphene.String()

    voided_by = graphene.String()
    date_voided = graphene.String()
    void_reason = graphene.String()
    county_district = graphene.String()
    address3 = graphene.String()

    address4 = graphene.String()
    address5 = graphene.String()
    address6 = graphene.String()
    date_changed = graphene.String()
    changed_by = graphene.String()

    uuid = graphene.String()
    facility = graphene.String()
    state = graphene.String()


class Query(graphene.ObjectType):
    obs = graphene.List(Obs, )
    encounter = graphene.List(Encounter, )
    encounter_provider = graphene.List(EncounterProvider, )
    person = graphene.List(Person, )
    patient = graphene.List(Patient, )
    person_name = graphene.List(PersonName, )
    person_attribute = graphene.List(PersonAttribute, )
    patient_identifier = graphene.List(PatientIdentifier, )
    visit = graphene.List(Visit, )
    person_address = graphene.List(PersonAddress, )

    @resolve_only_args
    def resolve_obs(self):
        data = db.query("select * from obs")
        all_data = [Obs(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_encounter(self):
        data = db.query("select * from encounter")
        all_data = [Encounter(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_encounter_provider(self):
        data = db.query("select * from encounter_provider")
        all_data = [EncounterProvider(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person(self):
        data = db.query("select * from person")
        all_data = [Person(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_patient(self):
        data = db.query("select * from patient")
        all_data = [Patient(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person_name(self):
        data = db.query("select * from person_name")
        all_data = [PersonName(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person_attribute(self):
        data = db.query("select * from person_attribute")
        all_data = [PersonAttribute(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_patient_identifier(self):
        data = db.query("select * from patient_identifier")
        all_data = [PatientIdentifier(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_visit(self):
        data = db.query("select * from visit")
        all_data = [Visit(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_person_address(self):
        data = db.query("select * from person_address")
        all_data = [PersonAddress(**d) for d in data]
        return all_data


schema = graphene.Schema(query=Query)
