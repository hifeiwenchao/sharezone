
from django.views import View
from api.service import auth, sms
from common.utils.http import formatting
import json


class SendRegisterSms(View):
    @formatting()
    def post(self, request):
        body = json.loads(request.body)
        phone = body['phone']
        sms.send_register_code(phone)


class SendLoginSms(View):
    @formatting()
    def post(self, request):
        body = json.loads(request.body)
        phone = body['phone']
        sms.send_login_code(phone)


class SendFindPwdSms(View):
    @formatting()
    def post(self, request):
        body = json.loads(request.body)
        phone = body['phone']
        sms.send_find_pwd_code(phone)


class SendResetPwdSms(View):
    @formatting()
    def post(self, request):
        body = json.loads(request.body)
        phone = body['phone']
        sms.send_reset_pwd_code(phone)




