import graphene

from core.database import Database

db = Database()


class TransferedPatient(graphene.ObjectType):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    id = graphene.ID()
    patient = graphene.String()
    transfered_in = graphene.String()
    tranfered_in_from = graphene.String()
    transfer_in_date = graphene.DateTime()
    transfered_out = graphene.String()
    tranfered_out_from = graphene.String()
    transfer_out_date = graphene.DateTime()