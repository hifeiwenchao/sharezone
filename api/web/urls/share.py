from django.urls import path

from api.web.share import Shares


urlpatterns = [
    path('shares', Shares.as_view()),


]
