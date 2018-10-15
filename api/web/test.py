
from django.views import View
from django.http.response import HttpResponse
from api.service import auth
from common.utils.http import formatting
import json
from api.utils import check_token


class Test(View):

    @formatting()
    def get(self, request):
        token = request.META.get('HTTP_TOKEN')
        print(token)
        result = check_token(token)
        return result

