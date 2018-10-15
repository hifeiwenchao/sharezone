from django.urls import path

from api.web.demand import Demands


urlpatterns = [
    path('demands', Demands.as_view()),


]

