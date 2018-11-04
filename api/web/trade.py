from django.views import View
from common.utils.http import formatting
from api.auth.decorator import auth
import json
from api import service
from api.utils.alipay import AliPayProxy


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


class Pay(View):
    @formatting()
    @auth
    def post(self, request):
        """
        支付
        :param request:
        :return:
        """
        user = request.user
        body = json.loads(request.body)
        order_id = body.get('order_id')
        pay_method = body.get('pay_method')
        device = body.get('device')
        if device == 'mobile':
            # 移动端返回支付参数用于调起支付APP
            return service.trade.app_pay(user, order_id, pay_method)
        else:
            # web端返回带参数的url
            return service.trade.page_pay(user, order_id, pay_method)
