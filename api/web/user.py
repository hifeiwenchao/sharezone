from api import service
from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
import ujson
from django.db import transaction
from rest_framework.views import APIView
from api.core.serializers import UserSerializer
from api.forms import user_form
from api.exceptions.defines import ArgumentsInvalidException
from common.utils.http import response_format
from rest_framework.response import Response
from api.views import BaseView


class SignIn(BaseView):
    @formatting()
    @auth
    def post(self, request):
        """
        签到
        :param request:
        :return:
        """
        return service.sign_in.sign_in(request.user)


class Profile(BaseView):
    forms_classes = (user_form.GetProfileForm,)

    @formatting()
    def get(self, request):
        """
        获取用户信息
        :param request:
        :return:
        """
        print('get is running...')
        params = request.query_params
        uid = params.get('uid')
        user = service.user.get_profile(uid)
        return UserSerializer(user).data

    @formatting()
    @auth
    def post(self, request):
        """
        编辑个人信息
        :param request:
        :return:
        """
        user = request.user
        data = request.data
        service.user.update_profile(user, **data)


class Avatar(BaseView):
    @formatting()
    @auth
    def post(self, request):
        """
        更换头像
        :param request:
        :return:
        """
        avatar = request.FILES.get('avatar')

        return service.user.change_avatar(request.user, avatar)

