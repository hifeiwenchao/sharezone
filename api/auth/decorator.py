
from django.contrib.auth import authenticate
from api.exceptions.defines import ForbiddenException


def auth(method):
    def wrapper(self, request, *args, **kwargs):
        token = request.META.get('HTTP_TOKEN')
        print('token: ', token)
        user = authenticate(token=token)
        if not user:
            raise ForbiddenException('请重新登录')
        request.user = user
        result = method(self, request, *args, **kwargs)
        return result
    return wrapper



