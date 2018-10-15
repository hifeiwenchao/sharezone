from django.urls import path

from api.web.sms import SendRegisterSms, SendLoginSms, SendFindPwdSms, SendResetPwdSms

urlpatterns = [
    path('register', SendRegisterSms.as_view()),
    path('login', SendLoginSms.as_view()),
    path('reset_pwd', SendResetPwdSms.as_view()),
    path('find_pwd', SendFindPwdSms.as_view()),


]

