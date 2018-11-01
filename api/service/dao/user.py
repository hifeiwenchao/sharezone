
from api.models import User
from django.db.models import Count


def get_users(**kwargs):
    return User.objects.filter(**kwargs)


def get_user(**kwargs):
    return User.objects.filter(**kwargs).first()


def exists(**kwargs):
    return User.objects.filter(**kwargs).exists()


def create_user(**kwargs):
    return User.objects.create(**kwargs)


def update(**kwargs):
    return User.objects.update(**kwargs)

