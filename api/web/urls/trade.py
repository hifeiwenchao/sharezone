from django.urls import path

from api.web.trade import Orders, Pay


urlpatterns = [
    path('orders', Orders.as_view()),
    path('order/pay', Pay.as_view()),


]
