import graphene

from core.database import Database
from core.schemas.facility import Facility

db = Database()


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

    person_attribute_facility = graphene.Field(Facility, )

    def resolve_person_attribute_facility(self, args, *_):
        data = db.query_one("select * from facility where uuid ='" + self.facility + "'")
        all_data = Facility(**data)
        return all_data