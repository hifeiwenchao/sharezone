#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from common import utils
from alipay.aop.api.AlipayClientConfig import AlipayClientConfig
from alipay.aop.api.DefaultAlipayClient import DefaultAlipayClient
from alipay.aop.api.FileItem import FileItem
from alipay.aop.api.domain.AlipayTradeAppPayModel import AlipayTradeAppPayModel
from alipay.aop.api.domain.AlipayTradePagePayModel import AlipayTradePagePayModel
from alipay.aop.api.domain.AlipayTradePayModel import AlipayTradePayModel
from alipay.aop.api.domain.GoodsDetail import GoodsDetail
from alipay.aop.api.domain.SettleDetailInfo import SettleDetailInfo
from alipay.aop.api.domain.SettleInfo import SettleInfo
from alipay.aop.api.domain.SubMerchant import SubMerchant
from alipay.aop.api.request.AlipayOfflineMaterialImageUploadRequest import AlipayOfflineMaterialImageUploadRequest
from alipay.aop.api.request.AlipayTradeAppPayRequest import AlipayTradeAppPayRequest
from alipay.aop.api.request.AlipayTradePagePayRequest import AlipayTradePagePayRequest
from alipay.aop.api.request.AlipayTradePayRequest import AlipayTradePayRequest
from alipay.aop.api.response.AlipayOfflineMaterialImageUploadResponse import AlipayOfflineMaterialImageUploadResponse
from alipay.aop.api.response.AlipayTradePayResponse import AlipayTradePayResponse
from django.conf import settings


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')

_APP_ID = utils.config('AliPay', 'app_id')
_PRIVATE_KEY = utils.config('AliPay', 'app_private_key')
_PUBLIC_KEY = utils.config('AliPay', 'public_key')


class AliPayProxy(object):
    """
    https://pypi.org/project/alipay-sdk-python/
    """
    def __init__(self):
        """
        得到客户端对象。
        注意，一个alipay_client_config对象对应一个DefaultAlipayClient
        定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
        logger参数用于打印日志，不传则不打印，建议传递。
        """
        alipay_client_config = AlipayClientConfig()
        alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
        alipay_client_config.app_id = _APP_ID
        alipay_client_config.app_private_key = _PRIVATE_KEY
        alipay_client_config.alipay_public_key = _PUBLIC_KEY

        self.client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

    @staticmethod
    def _expire_time():
        """
        将settings中的超时时间(秒)转化成支付宝可用的格式(1m～15d。m-分钟，h-小时，d-天)
        :return:
        """
        expire_time = settings.PAYMENT_EXPIRE_TIME
        if expire_time % (24 * 3600) == 0:
            return '%sd' % (int(expire_time / (24 * 3600)))
        if expire_time % 3600 == 0:
            return '%sh' % (int(expire_time / 3600))
        if expire_time % 60 == 0:
            return '%sm' % (int(expire_time / 60))

    def trade_app_pay(self, **kwargs):
        model = AlipayTradeAppPayModel()
        model.timeout_express = self._expire_time()
        model.total_amount = kwargs.get('total_amount')
        model.product_code = "QUICK_MSECURITY_PAY"
        model.body = kwargs.get('body')
        model.subject = kwargs.get('subject')
        model.out_trade_no = kwargs.get('out_trade_no')
        request = AlipayTradeAppPayRequest(biz_model=model)
        response = self.client.sdk_execute(request)
        return response

    def trade_page_pay(self, **kwargs):
        model = AlipayTradePagePayModel()
        model.timeout_express = self._expire_time()
        model.out_trade_no = kwargs.get('out_trade_no')
        model.total_amount = kwargs.get('total_amount')
        model.subject = kwargs.get('subject')
        model.body = kwargs.get('body')
        model.product_code = "FAST_INSTANT_TRADE_PAY"
        request = AlipayTradePagePayRequest(biz_model=model)
        # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
        response = self.client.page_execute(request, http_method="GET")
        return response
