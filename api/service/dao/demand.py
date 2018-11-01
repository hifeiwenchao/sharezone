from api.models import Demand
from django.db.models import Count


def create(**kwargs):
    return Demand.objects.create(**kwargs)


def get_demand(**kwargs):
    return Demand.objects.filter(**kwargs).first()


def get_demands(**kwargs):
    return Demand.objects.filter(**kwargs).all()


def demand_count(user):
    return Demand.objects.all().annotate(demand_count=Count("user"))
