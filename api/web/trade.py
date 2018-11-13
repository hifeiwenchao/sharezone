from django.views import View
from rest_framework.views import APIView
from common.utils.http import formatting
from api.auth.decorator import auth
import ujson
from api import service
from api.jobs import close_order
from api.utils.alipay import AliPayProxy
from django.conf import settings
from api.views import BaseView


import logging
logger = logging.getLogger('api')


class Orders(BaseView):
    @formatting()
    @auth
    def post(self, request):
        """
        提交订单
        :param request:
        :return:
        """
        user = request.user
        data = request.data
        share_id = data.get('share_id')
        number = data.get('number')
        start_at = data.get('start_at')
        end_at = data.get('end_at')
        is_use_pool = data.get('is_use_pool', True)
        message = data.get('message')
        trade_method = data.get('trade_method', 1)
        order = service.trade.gen_order(user, share_id, number, start_at, end_at, is_use_pool, message, trade_method)
        close_order.apply_async(args=(order.id,), countdown=settings.PAYMENT_EXPIRE_TIME, queue='default')
        return order.id


class Pay(BaseView):
    @formatting()
    @auth
    def post(self, request):
        """
        支付
        :param request:
        :return:
        """
        user = request.user
        data = request.data
        order_id = data.get('order_id')
        pay_method = data.get('pay_method')
        is_mobile = data.get('is_mobile', True)
        return service.trade.pay(user, order_id, pay_method, is_mobile)


class Notify(BaseView):
    @formatting()
    def post(self, request, pay_method):
        if pay_method == 'alipay':
            logger.info(request.data)
            logger.info('alipay')
        elif pay_method == 'wechat':
            logger.info(request.data)
            logger.info('wechat')
        else:
            logger.info(request.data)
            logger.info('error...')

    def get(self, request, pay_method):
        if pay_method == 'alipay':
            logger.info(request.query_params)
            logger.info('alipay')
        elif pay_method == 'wechat':
            logger.info(request.query_params)
            logger.info('wechat')
        else:
            logger.info(request.query_params)
            logger.info('error...')
