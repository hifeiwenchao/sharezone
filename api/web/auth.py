
from django.views import View
from api.service import auth
from common.utils.http import formatting
from common import utils
import ujson


class Login(View):
    @formatting()
    def post(self, request):
        body = ujson.loads(request.body)
        phone = body['phone']
        password = body['password']
        result = auth.login(phone, password)

        return {'token': result}


class SmsLogin(View):
    @formatting()
    def post(self, request):
        print(request.body)
        body = ujson.loads(request.body)
        phone = body['phone']
        code = body['code']
        result = auth.sms_login(phone, code)
        return {'token': result}


class Register(View):
    @formatting()
    def post(self, request):
        body = ujson.loads(request.body)
        phone = body.get('phone')
        code = body.get('code')
        password = body.get('password')

        return auth.register(phone, password, code)


class UpdatePassword(View):
    @formatting()
    def post(self, request):
        body = ujson.loads(request.body)
        phone = body.get('phone')
        code = body.get('code')
        password = body.get('password')
        auth.find_password(phone, code, password)



