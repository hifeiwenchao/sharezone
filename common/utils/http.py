import functools
from django.http import HttpResponse
import json
from common.utils import obj2dict
from api.exceptions.defines import ApiBaseException
from django.contrib.auth import authenticate
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.core.serializers.json import DjangoJSONEncoder


def response_format(code=0, data=None, message=""):
    if data is None:
        data = data
    elif isinstance(data, (str, int, float, list, dict, tuple)):
        data = data
    elif isinstance(data, QuerySet):
        data = serialize('json', data, cls=DjangoJSONEncoder)
        data = json.loads(data)
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
                token = args[0].META.get('HTTP_ACCESS_TOKEN')
                user = authenticate(token=token)
                args[0].user = user
                data = method(self, *args, **kwargs)
            except Exception as e:
                raise
            return response_format(data=data)
        return wrapper
    return decorator
