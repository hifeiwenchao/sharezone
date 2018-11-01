from django.utils.deprecation import MiddlewareMixin
from django.http.response import HttpResponse
from api.exceptions.defines import ApiBaseException
import json
from common.utils.http import response_format


class CommonMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        print('process response...')
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ApiBaseException):
            return response_format(code=exception.code, message=exception.message)
        # return response_format(code=500, message='服务器发生未知错误')
