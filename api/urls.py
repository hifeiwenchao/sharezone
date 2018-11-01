from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.conf import settings

from api.web.test import Test


urlpatterns = [
    path('auth/', include('api.web.urls.auth')),
    path('test', Test.as_view()),
    path('sms/', include('api.web.urls.sms')),
    path('user/', include('api.web.urls.user')),
    path('demand/', include('api.web.urls.demand')),
    path('share/', include('api.web.urls.share')),
    path('trade/', include('api.web.urls.trade')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
