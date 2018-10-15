
from api.models import UserInfo
from common import utils
import random


def create_user_info(**kwargs):
    return UserInfo.objects.create(**kwargs)


def add_integral(user, integral):
    user_info = UserInfo.objects.filter(user=user).first()
    user_info.integral += integral
    user_info.save()


def gen_nickname():
    return 'yiqi' + str(utils.current_timestamp())[-11:] + str(random.randint(100000, 1000000))

