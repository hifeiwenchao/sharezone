from django.utils.deprecation import MiddlewareMixin
from api.exceptions.defines import ApiBaseException
from common.utils.http import response_format
import traceback
import logging


logger = logging.getLogger('api')


class CommonMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response

    def process_exception(self, request, exception):
        logger.error(traceback.format_exc())
        if isinstance(exception, ApiBaseException):
            return response_format(code=exception.code, message=exception.message)
        return response_format(code=500, message='服务器发生未知错误')
