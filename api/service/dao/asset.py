
from api.models import Asset


def create(**kwargs):
    return Asset.objects.create(**kwargs)


