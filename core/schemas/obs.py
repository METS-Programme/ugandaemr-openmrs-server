import graphene

from core.database import Database
from core.schemas.encounter import Encounter

db = Database()


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
