from api.service import dao
from api.utils import check_token
from api.exceptions.defines import InvalidCodeException
from api.const import SmsTemplateCode, SmsExpire


class PasswordBackend(object):
    def authenticate(self, request, phone=None, password=None):
        if phone and password:
            user = dao.user.get_user(phone=phone)
            if user and user.check_password(password):
                return user
        return None

    def get_user(self, uid):
        return dao.user.get_user(id=uid)


class SmsCodeBackend(object):
    def authenticate(self, request, phone=None, code=None):
        # 检测验证码
        valid = dao.identity_code.is_valid_code(phone, code, SmsTemplateCode.LOGIN)
        if not valid:
            raise InvalidCodeException()
        if dao.user.exists(phone=phone):
            # 用户已注册过，并验证码正确，允许登录
            user = dao.user.get_user(phone=phone)
        else:
            # 第一次登录，生成用户相关信息
            user = dao.user.create_user(phone=phone)
            nickname = dao.user_info.gen_nickname()
            dao.user_info.create(nickname=nickname, user=user)
            dao.deposit_pool.create(user=user)
            dao.asset.create(user=user)
        return user

    def get_user(self, uid):
        return dao.user.get_user(id=uid)


class TokenBackend(object):
    def authenticate(self, request, token=None):
        uid = check_token(token)
        if uid:
            user = dao.user.get_user(id=uid)
            return user
        return None

    def get_user(self, uid):
        return dao.user.get_user(id=uid)
