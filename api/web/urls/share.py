from django.urls import path, re_path

from api.web.share import Shares, Share, PublicShares


urlpatterns = [
    path('shares', Shares.as_view()),
    re_path('^shares/(?P<share_id>\d+)$', Share.as_view()),
    path('shares/public', PublicShares.as_view()),

]
