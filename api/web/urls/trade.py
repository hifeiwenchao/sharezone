from django.urls import path

from api.web.trade import Orders


urlpatterns = [
    path('orders', Orders.as_view()),


]
