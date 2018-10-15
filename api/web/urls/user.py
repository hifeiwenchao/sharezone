from django.urls import path

from api.web.user import SignIn

urlpatterns = [
    path('sign_in', SignIn.as_view()),


]

