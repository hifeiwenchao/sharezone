from django.urls import path, include

from api.web.test import Test

urlpatterns = [
    path('auth/', include('api.web.urls.auth')),
    path('test', Test.as_view()),
    path('sms/', include('api.web.urls.sms')),
    path('user/', include('api.web.urls.user')),
    path('demand/', include('api.web.urls.demand'))


]

