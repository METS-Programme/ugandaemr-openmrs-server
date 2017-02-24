import graphene

from core.database import Database

db = Database()


class Encounter(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

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
