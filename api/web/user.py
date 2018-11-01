from api import service
from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
import json
from django.db import transaction


class SignIn(View):
    @formatting()
    @auth
    def post(self, request):
        """
        签到
        :param request:
        :return:
        """
        return service.sign_in.sign_in(request.user)


class Profile(View):
    @formatting()
    def get(self, request):
        """
        获取用户信息
        :param request:
        :return:
        """
        uid = request.GET.get('uid')
        profile = service.user.get_profile(uid)
        return profile

    @formatting()
    @auth
    def post(self, request):
        """
        编辑个人信息
        :param request:
        :return:
        """
        user = request.user
        body = json.loads(request.body)
        service.user.update_profile(user, **body)


class Avatar(View):
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

