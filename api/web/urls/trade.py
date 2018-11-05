from django.urls import path, re_path

from api.web.trade import Orders, Pay, Notify


urlpatterns = [
    path('orders', Orders.as_view()),
    path('order/pay', Pay.as_view()),
    re_path('^order/pay/notify/(?P<pay_method>(?:alipay|wechat))$', Notify.as_view()),


]
