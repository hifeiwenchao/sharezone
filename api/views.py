from rest_framework.views import APIView
from api.exceptions.defines import ArgumentsInvalidException, ApiBaseException
from common.utils.http import response_format


class BaseView(APIView):
    forms_classes = ()

    def initial(self, request, *args, **kwargs):
        for form_class in self.forms_classes:
            if request.method in form_class.http_methods:
                if request.method == 'GET':
                    arguments = request.query_params
                else:
                    arguments = request.data
                fc = form_class(arguments)
                if not fc.is_valid():
                    raise ArgumentsInvalidException()
        super(BaseView, self).initial(request, *args, **kwargs)

    def handle_exception(self, exc):
        if isinstance(exc, ApiBaseException):
            return response_format(code=500, message=exc.message)
        super(BaseView, self).handle_exception(exc)
