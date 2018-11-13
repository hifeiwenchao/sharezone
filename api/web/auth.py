
from rest_framework.views import APIView
from api.service import auth
from common.utils.http import formatting
from common import utils
import ujson
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from api.core.serializers import UserSerializer
from api.views import BaseView
from api.forms.auth_form import PostLoginForm


class Login(BaseView):
    forms_classes = (PostLoginForm,)

    @formatting()
    def post(self, request):
        data = request.data
        phone = data['phone']
        password = data['password']
        result = auth.login(phone, password)
        return {'token': result}


class SmsLogin(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data['phone']
        code = data['code']
        result = auth.sms_login(phone, code)
        return {'token': result}


class Register(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data.get('phone')
        code = data.get('code')
        password = data.get('password')

        user = auth.register(phone, password, code)
        return UserSerializer(user).data


class UpdatePassword(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data.get('phone')
        code = data.get('code')
        password = data.get('password')
        auth.find_password(phone, code, password)



