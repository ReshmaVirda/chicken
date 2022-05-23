from django.contrib import admin
from django.urls import path
from user_profile.views import CustomAuthToken, LogoutView,RegisterView
from django.urls import include, path

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("sign-up/", RegisterView.as_view()),

]
