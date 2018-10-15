
from api.models import IntegralLog


def create(**kwargs):
    return IntegralLog.objects.create(**kwargs)


