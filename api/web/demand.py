from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
import ujson
from api import service
from api.core.serializers import DemandSerializer


class Demands(View):
    @formatting()
    @auth
    def post(self, request):
        """
        发布需求
        :param request:
        :return:
        """
        body = ujson.loads(request.body)
        demand = service.demand.publish(request.user, **body)
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
