#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import traceback

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

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filemode='a',)
logger = logging.getLogger('')


class AliPayProxy(object):
    """
    https://pypi.org/project/alipay-sdk-python/
    """

    def __init__(self):
        alipay_client_config = AlipayClientConfig()
        alipay_client_config.server_url = 'https://openapi.alipay.com/gateway.do'
        alipay_client_config.app_id = '2018012302039707'
        alipay_client_config.app_private_key = 'MIIEowIBAAKCAQEAzatbMRSR3WeNuIf+C1+pQOmcUfWCgov3ONin/Z7cByKRnJGQTYCvFCVak9rrSF/v9Y+j0+JSN4SaY4L4ro0gzkNJ7lKBh010RMUfGgN5UED3n3IliFSWlq2YadcmphzZ3PLVn4RkFJaqHe2PvaUoFHZEshiZBVkGehjYB4kNyekL4WAoJzA/Xzfqm7/QBUfs2taXXBRu0SQaVM2xflEmFXELQyJfE681TvyRbXgf1u0KCcYKrnQ13UxB5IyHMnqvPSff4QI0tznBjPuvO0ZxV/Z5jbmW9dqP8NS/a4/9TlKPAxe+GNElFUJ1tT1bm8PBeQjkwLdrgPKSlUv5flk2NQIDAQABAoIBAQCAc0wiDCnJsNonbO/yZI2N2BlkasRXClmeLFpHIUdkQWfV9Ge+r+co2ueGPo0CB8ETieGU/N3ChNPz4KG2Srg5encbHHZ/bZV3OfHhylejEuBUufLNAZ+HfeYZ/GDMEGrU/ukClqn23d5jkLJcjGDK3s6quIgheed8rDWIB0YQWpkNEv9COr5jyiVxiAtzegF87wMwdkvBOAg810ILJCh+dAfMnfjHFfAOv46hJqWM3Hsvth5Dnf4ieJhIYx0BzuQCRXb6i1d4fCKoV3Em7mreHPPB5aAzSJuc+8mNNwzLNg23MP+WgsoVyAxazYb9a8Sr+/Xno0KvlXuO5PIGEIEFAoGBAOWDBkJ7tKXTez9X9tkfU5ubx89zVOJlWfg/S4JB+6aCx00iF19kiGN5c6zRUTUgXXVsAGcSagp9sfXerecuoe1FmJ1x7wtM8XQGn75AjEaovbreAF3xIP4H8hEFS65LK+glxmHHqzre6mwnAG3USIV4oXIfTTvHtSABd1G6CiMbAoGBAOVn5sBEV00tCqXTUJkcHwEKN5pPuW/ELBfoqt0xoAjdxOqmefMplxEmUCaFXYt+FuUQ2Gimk6sXnBS9enhuZdVuByyRf0nKBxZGyEI42uqKvzjeHDebA4RHEYLUxCyS5CYgytkW8sMv9RD/004qomSM8xwfLYQ1mh5Ywr5AXlDvAoGAa+zbKrRFVJ1IHZddyugCRvBQW2sehX+neSc6eLxSfBCPa+QWHZOG11ArZx7fEx5vFGJ/JfjwyJIm9zmJiWbSWmMZyx/iiuvZtvfOcoaj8C41WgQ/I+3Z19sgp4RX/FP5B6eLzDs6d+qPTeBhQURL/gel06aIiQ32TGCkHVhgn/UCgYARa+eROF9s4/vIBhk712/fU1hPprhNbZdvpWK8c5VUtwrKSyQ9vC3VxpQVqNEm08eHU9UrdWMHfj6DMLSJStD++WEgGFiTUP1iyrNQnCK75xeIiQ2Zh3Mn64G/7sqLHAipgJoHDIAZJJ420UbJy+ETQ8T+oLuDK9LtdQ4tBpRjDwKBgEqm2RmevHlNcJOWyL6nAd48XWsWWbKgoMj9qnC48ep/R7oQ4CIjJh77yF9Dp6b50skkyDzS9mjDpetCzSCJx1i4M1fQGg5diQqIG6VhpKtKvCI5c/uWkhFsqvK5TLV1Wd+L7lbTDB/+iqttvDQ7C35fwHRkCVnG05DqL2WXv/33'
        alipay_client_config.alipay_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAgcuJpmrJG7Jt4lT//whxMEcaf8glkXiVGqCtzZZVb/sAskbxadGjzfCEAKfYob69ETT9DRJwK63UpOUuH+Ts8S2Q3h2vRDcquCziKBxdOGgLFwxaVnsXFO6Cmasf4kKgaMxakwkNm6Y3rZ5gXSQ1OTH7gbsNoQ9Xkd3RpG9o8Ytj7NIupsGEqk30q/hzeoTBRuwPPfbvV5oC1kNj1YhebaTYQuaevCEDl+U8ti3OLXPlfwPYHu1ueQvGiQbKTuF1auk8cH6DW+Vtc7vvNWnMFafcy3qqFJrMKRsH3ynTtGmBWMnHen83Al3laEdwao26gZN2oFSbxKu0CXB7d1cSOQIDAQAB'

        """
        得到客户端对象。
        注意，一个alipay_client_config对象对应一个DefaultAlipayClient，定义DefaultAlipayClient对象后，alipay_client_config不得修改，如果想使用不同的配置，请定义不同的DefaultAlipayClient。
        logger参数用于打印日志，不传则不打印，建议传递。
        """
        self.client = DefaultAlipayClient(alipay_client_config=alipay_client_config, logger=logger)

    def trade_app_pay(self):
        # todo
        pass


if __name__ == '__main__':

    """
    页面接口示例：alipay.trade.page.pay
    """
    # 对照接口文档，构造请求对象
    model = AlipayTradePagePayModel()
    model.out_trade_no = "pay201805020000226"
    model.total_amount = 50
    model.subject = "测试"
    model.body = "支付宝测试"
    model.product_code = "FAST_INSTANT_TRADE_PAY"
    settle_detail_info = SettleDetailInfo()
    settle_detail_info.amount = 50
    settle_detail_info.trans_in_type = "userId"
    settle_detail_info.trans_in = "2088302300165604"
    settle_detail_infos = list()
    settle_detail_infos.append(settle_detail_info)
    settle_info = SettleInfo()
    settle_info.settle_detail_infos = settle_detail_infos
    model.settle_info = settle_info
    sub_merchant = SubMerchant()
    sub_merchant.merchant_id = "2088301300153242"
    model.sub_merchant = sub_merchant
    request = AlipayTradePagePayRequest(biz_model=model)
    # 得到构造的请求，如果http_method是GET，则是一个带完成请求参数的url，如果http_method是POST，则是一段HTML表单片段
    response = client.page_execute(request, http_method="GET")
    print("alipay.trade.page.pay response:" + response)


    """
    构造唤起支付宝客户端支付时传递的请求串示例：alipay.trade.app.pay
    """
    model = AlipayTradeAppPayModel()
    model.timeout_express = "90m"
    model.total_amount = "9.00"
    model.seller_id = "2088301194649043"
    model.product_code = "QUICK_MSECURITY_PAY"
    model.body = "Iphone6 16G"
    model.subject = "iphone"
    model.out_trade_no = "201800000001201"
    request = AlipayTradeAppPayRequest(biz_model=model)
    response = client.sdk_execute(request)
    print("alipay.trade.app.pay response:" + response)
