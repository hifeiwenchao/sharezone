
from api.service import dao
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate
from api.exceptions.defines import ForbiddenException, InvalidCodeException, ExistedException, NotFoundException
from api.const import SmsTemplateCode
from common import utils
from api.utils import check_token, make_token
import random
from django.core.cache import cache


def login(phone, password):
    """
    用户名密码登录
    :param str phone: 手机号
    :param str password: 密码
    :return:
    """
    user = authenticate(phone=phone, password=password)
    if user:
        token = make_token(user.id)
        return token

    raise ForbiddenException(message='用户名或密码错误')


def sms_login(phone, code):
    """
    短信验证码登录
    :param str phone: 手机号
    :param str code: 验证码
    :return:
    """
    user = authenticate(phone=phone, code=code)
    if user:
        return make_token(user.id)
    raise InvalidCodeException()


def register(phone, password, code):
    """
    注册
    :param str phone:
    :param str password:
    :param str code:
    :return:
    """
    valid = dao.identity_code.is_valid_code(phone, code, SmsTemplateCode.REGISTER)
    if valid:
        if dao.user.exists(phone=phone):
            raise ExistedException('用户已存在')

        password = make_password(password)
        username = dao.user_info.gen_username()
        user = dao.user.create_user(username=username, phone=phone, password=password)
        dao.user_info.create(user=user)

        dao.deposit_pool.create(user=user)
        dao.asset.create(user=user)

        return user
    raise InvalidCodeException()


def find_password(phone, code, password):
    valid = dao.identity_code.is_valid_code(phone, code, SmsTemplateCode.FIND_PWD)
    if valid:
        if not dao.user.exists(phone=phone):
            raise NotFoundException('账号不存在')
        dao.user.update(password=make_password(password), updated_at=utils.current_timestamp())
    else:
        raise InvalidCodeException()




