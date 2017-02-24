import graphene

from core.database import Database

db = Database()


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

