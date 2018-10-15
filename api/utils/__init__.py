from common import utils
from django.core.cache import cache


def make_token(uid):
    token = utils.encrypt({'uid': uid})
    cache.set('uid' + str(uid), token, 3600)
    return token


def check_token(token):
    if not token:
        return 0
    info = utils.decrypt(token)
    print('info: ', info)
    if info and isinstance(info, dict):
        uid = info['uid']
        saved_token = cache.get('uid' + str(uid))
        print('saved_token: ', saved_token)
        if saved_token == token:
            return uid
    return 0


