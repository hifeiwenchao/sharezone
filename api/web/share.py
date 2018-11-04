
from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
import json
from api import service
from api.const import ShareStatus


class Shares(View):
    @formatting()
    @auth
    def post(self, request):
        """
        发布共享
        :param request:
        :return:
        """
        body = json.loads(request.body)
        share = service.share.publish(request.user, **body)
        return share.id

    @formatting()
    @auth
    def get(self, request):
        """
        我发布的共享
        :param request:
        :return:
        """
        user = request.user
        shares = service.share.get_shares(user=user)
        return shares


class PublicShares(View):
    @formatting()
    def get(self, request):
        """
        所有用户已发布的共享
        :param request:
        :return:
        """
        shares = service.share.get_shares(status=ShareStatus.OPEN)
        return shares


class Share(View):
    @formatting()
    def get(self, request, share_id):
        """
        共享详情
        :param request:
        :param share_id:
        :return:
        """
        share = service.share.get_share(id=share_id)
        return share
