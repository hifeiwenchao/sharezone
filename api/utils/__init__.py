from common import utils
from django.core.cache import cache
from django.conf import settings


def make_token(uid):
    token = utils.encrypt({'uid': uid})
    expire_time = settings.TOKEN_EXPIRE_TIME
    if settings.DEBUG:
        expire_time = 3600 * 10

    cache.set('uid' + str(uid), token, expire_time)
    return token


def check_token(token):
    if not token:
        return 0
    info = utils.decrypt(token)
    if info and isinstance(info, dict):
        uid = info['uid']
        saved_token = cache.get('uid' + str(uid))
        if saved_token == token:
            return uid
    return 0


