from django.contrib import admin
from django.urls import path
from user_profile.views import (
    CustomAuthToken,
    LogoutView,
    RegisterView,
    UserAPIView,
    FileUploadView,
    
)
from user_profile.views import ForgotPasswordRequest,ForgotPasswordView
from django.urls import include, path

urlpatterns = [
    path("api-token-auth/", CustomAuthToken.as_view()),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("sign-up/", RegisterView.as_view()),
    path("user/", UserAPIView.as_view()),
    path(
        "profile-image-upload/",
        FileUploadView.as_view(),
    ),
    path(
        "forgot-password-request/",
        ForgotPasswordRequest.as_view(),
    ),
    path(
        "forgot-password/",
        ForgotPasswordView.as_view(),
    ),
]
