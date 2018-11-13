
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


class Login(APIView):
    @formatting()
    def post(self, request):
        body = ujson.loads(request.body)
        phone = body['phone']
        password = body['password']
        result = auth.login(phone, password)

        return {'token': result}


class SmsLogin(APIView):
    @formatting()
    def post(self, request):
        print(request.body)
        body = ujson.loads(request.body)
        phone = body['phone']
        code = body['code']
        result = auth.sms_login(phone, code)
        return {'token': result}


class Register(APIView):
    @formatting()
    def post(self, request):
        body = ujson.loads(request.body)
        phone = body.get('phone')
        code = body.get('code')
        password = body.get('password')

        user = auth.register(phone, password, code)
        return UserSerializer(user).data


class UpdatePassword(APIView):
    @formatting()
    def post(self, request):
        body = ujson.loads(request.body)
        phone = body.get('phone')
        code = body.get('code')
        password = body.get('password')
        auth.find_password(phone, code, password)



