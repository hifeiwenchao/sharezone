from django.urls import path

from api.web.share import Shares, PublicShares


urlpatterns = [
    path('shares', Shares.as_view()),
    path('shares/public', PublicShares.as_view()),


]
