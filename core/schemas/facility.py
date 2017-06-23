import graphene

from core.database import Database

db = Database()


class Facility(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()
    uuid = graphene.String()
    name = graphene.String()