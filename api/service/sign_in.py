from api.service import dao
from api import const
from api.exceptions.defines import ApiBaseException


def sign_in(user):
    # 检测当天是否已经签到
    if dao.sign_log.check_sign(user):
        raise ApiBaseException('已经签到过了')
    dao.sign_log.create(user=user)
    dao.integral_log.create(user=user, integral=const.SIGN_IN_INTEGRAL)
    dao.user_info.add_integral(user, const.SIGN_IN_INTEGRAL)
    return const.SIGN_IN_INTEGRAL

