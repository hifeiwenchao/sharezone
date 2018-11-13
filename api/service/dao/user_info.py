
from api.models import UserInfo
from common import utils
import random
from django.db.models import F


def gen_username():
    return 'yiqi' + str(utils.current_timestamp())[-11:] + str(random.randint(100000, 1000000))


def create(**kwargs):
    return UserInfo.objects.create(**kwargs)


def add_integral(user, integral):
    return UserInfo.objects.filter(user=user).update(integral=F('integral')+integral)


def exists(**kwargs):
    return UserInfo.objects.filter(**kwargs).exists()


def is_valid_nickname(nickname, user=None):
    query = UserInfo.objects.filter(nickname=nickname)
    if user is not None:
        query.exclude(user=user)
    return not query.exists()


def update(user, **kwargs):
    return UserInfo.objects.filter(user=user).update(**kwargs)

