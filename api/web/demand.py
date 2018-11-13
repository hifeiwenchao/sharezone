from django.views import View
from rest_framework.views import APIView
from common.utils.http import formatting
from api.auth.decorator import auth
import ujson
from api import service
from api.core.serializers import DemandSerializer
from api.views import BaseView


class Demands(BaseView):
    @formatting()
    @auth
    def post(self, request):
        """
        发布需求
        :param request:
        :return:
        """
        data = request.data
        demand = service.demand.publish(request.user, **data)
        return DemandSerializer(demand).data

    @formatting()
    @auth
    def get(self, request):
        """
        我发布的需求
        :param request:
        :return:
        """
        user = request.user
        demands = service.demand.get_demands(user=user)
        return [DemandSerializer(demand).data for demand in demands]
