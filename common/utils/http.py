import functools
from django.http import HttpResponse
import json
from common.utils import obj2dict
from api.exceptions.defines import ApiBaseException


def response_format(code=200, data=None, message=""):
    if data is None:
        data = data
    elif isinstance(data, (str, int, float, list, dict, tuple)):
        data = data
    else:
        data = obj2dict(data)

    response = {"message": message, "data": data, "code": code}
    response = json.dumps(response, ensure_ascii=False, indent=4)
    return HttpResponse(content=response, content_type='application/json')


def formatting(input=None, output=None):
    """
    :param input: request接口参数校验form
    :param output: response接口参数校验form
    :return:
    """
    def decorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            try:
                data = method(self, *args, **kwargs)
            except Exception as e:
                raise
            return response_format(data=data)
        return wrapper
    return decorator
