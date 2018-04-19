import graphene
from core.database import Database

db = Database()


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
