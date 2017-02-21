import graphene
from graphene import relay
from graphene import resolve_only_args
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from core.sql_queries import query_one
from database import Database

import types

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


class Patient(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

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


class Encounter(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()

    encounter_type = graphene.String()
    patient = graphene.Field(Patient)
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
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()
    person = graphene.String()
    concept = graphene.String()
    encounter = graphene.Field(Encounter)
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


class EncounterProvider(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()
    encounter = graphene.String()
    provider = graphene.String()
    encounter_role = graphene.String()
    creator = graphene.String()
    date_created = graphene.String()

    uuid = graphene.String()


class PersonName(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

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
    def __init__(self, **entries):
        self.__dict__.update(entries)

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
    def __init__(self, **entries):
        self.__dict__.update(entries)

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
    def __init__(self, **entries):
        self.__dict__.update(entries)

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
    def __init__(self, **entries):
        self.__dict__.update(entries)

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


def get_one(**query_info):
    return db.query_one_with_data(query_one, query_info)


def get_foreign_keys(sql_data, *argv):
    for d in sql_data:
        for arg in argv:
            foreign_table = arg['foreign_table']
            primary_column = arg['primary_column']
            class_name = arg['class_name']
            graph_prop = arg['graph_prop']
            primary_value = d[primary_column]
            if primary_value is not None:
                data = get_one(table_name=foreign_table, primary_column='uuid', primary_value=primary_value)
                d[graph_prop] = eval(class_name)(**data)
    return sql_data


def str_to_class(s):
    if s in globals() and isinstance(globals()[s], types.ClassType):
        return globals()[s]
    return None


class Query(graphene.ObjectType):
    obs = graphene.List(Obs, )
    encounters = graphene.List(Encounter, )
    encounter_providers = graphene.List(EncounterProvider, )
    persons = graphene.List(Person, )
    patients = graphene.List(Patient, )
    person_names = graphene.List(PersonName, )
    person_attributes = graphene.List(PersonAttribute, )
    patient_identifiers = graphene.List(PatientIdentifier, )
    visits = graphene.List(Visit, )
    person_addresses = graphene.List(PersonAddress, )
    person = graphene.Field(Person, id=graphene.String())

    @resolve_only_args
    def resolve_obs(self):
        data = db.query("select * from obs")
        all_data = [Obs(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_encounters(self):
        data = db.query("select * from encounter")

        data = get_foreign_keys(data, *[{
            'foreign_table': 'patient', 'foreign_key': 'patient_id', 'primary_column': 'patient_id',
            'class_name': 'Patient', 'graph_prop': 'patient'
        }])

        all_data = [Encounter(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_encounter_providers(self):
        data = db.query("select * from encounter_provider")
        all_data = [EncounterProvider(**d) for d in data]
        return all_data

    @resolve_only_args
    def resolve_persons(self):
        data = db.query("select * from person")
        data = get_foreign_keys(data, *[{
            'foreign_table': 'users', 'foreign_key': 'user_id', 'primary_column': 'creator'
        }])

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


schema = graphene.Schema(query=Query)
