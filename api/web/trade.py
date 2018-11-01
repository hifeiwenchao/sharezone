from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
import json
from api import service


class Orders(View):
    @formatting()
    @auth
    def post(self, request):
        """
        提交订单
        :param request:
        :return:
        """
        user = request.user
        body = json.loads(request.body)
        share_id = body.get('share_id')
        number = body.get('number')
        start_at = body.get('start_at')
        end_at = body.get('end_at')
        is_use_pool = body.get('is_use_pool', True)
        message = body.get('message')
        trade_method = body.get('trade_method', 1)
        order = service.trade.gen_order(user, share_id, number, start_at, end_at, is_use_pool, message, trade_method)
        return order.id
