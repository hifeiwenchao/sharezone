from django.urls import path

from api.web.user import SignIn, Profile, Avatar

urlpatterns = [
    path('sign_in', SignIn.as_view()),
    path('profile', Profile.as_view()),
    path('avatar', Avatar.as_view()),


]
