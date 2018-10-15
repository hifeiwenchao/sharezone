from api.models import Demand


def create(**kwargs):
    return Demand.objects.create(**kwargs)


def get_demand(**kwargs):
    return Demand.objects.filter(**kwargs).first()


def get_demands(**kwargs):
    return Demand.objects.filter(**kwargs)




