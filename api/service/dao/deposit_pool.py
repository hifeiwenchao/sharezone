
from api.models import DepositPool


def create(**kwargs):
    return DepositPool.objects.create(**kwargs)


