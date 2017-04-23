import graphene

from core.database import Database
from core.schemas.facility import Facility
from core.schemas.obs import Obs

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

    obs = graphene.List(Obs, )

    def resolve_encounter_facility(self, args, *_):
        data = db.query_one("select * from facility where uuid ='" + self.facility + "'")
        all_data = Facility(**data)
        return all_data

    def resolve_obs(self, args, *_):
        data = db.query(
            "select o.*,e.encounter_datetime as encounter_date,e.encounter_type as encounter_type from obs o inner join encounter e on(o.encounter = e.uuid and o.encounter ='" + self.uuid + "')")
        all_data = [Obs(**d) for d in data]
        return all_data
