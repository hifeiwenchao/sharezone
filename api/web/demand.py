from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
# from api.service import demand
import json
import api.service.demand


class Demands(View):
    @formatting()
    @auth
    def post(self, request):
        body = json.loads(request.body)
        demand = api.service.demand.publish(request.user, **body)
        return demand

    @formatting()
    @auth
    def get(self, request):
        return 'get demands'


