from django.urls import path

from api.web.auth import Login, SmsLogin, Register, UpdatePassword

urlpatterns = [
    path('login', Login.as_view()),
    path('sms_login', SmsLogin.as_view()),
    path('register', Register.as_view()),
    path('update_password', UpdatePassword.as_view()),


]

