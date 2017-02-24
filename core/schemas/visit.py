import graphene


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
