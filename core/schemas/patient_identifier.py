import graphene

from core.database import Database

db = Database()


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
