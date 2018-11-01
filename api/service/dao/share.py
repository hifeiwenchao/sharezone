from api.models import Share


def create(**kwargs):
    return Share.objects.create(**kwargs)


def get_share(**kwargs):
    return Share.objects.filter(**kwargs).first()


def get_shares(**kwargs):
    return Share.objects.filter(**kwargs)

