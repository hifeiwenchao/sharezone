
from django.views import View
from api.service import auth, sms
from common.utils.http import formatting
from rest_framework.views import APIView
from api.views import BaseView
import ujson


class SendRegisterSms(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data['phone']
        sms.send_register_code(phone)


class SendLoginSms(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data['phone']
        sms.send_login_code(phone)


class SendFindPwdSms(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data['phone']
        sms.send_find_pwd_code(phone)


class SendResetPwdSms(BaseView):
    @formatting()
    def post(self, request):
        data = request.data
        phone = data['phone']
        sms.send_reset_pwd_code(phone)
