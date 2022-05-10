from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from django.conf import settings

# Create your views here.
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        request.data["username"] = request.data["mobile_no"]

        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():

            user = User.objects.get(
                username=serializer.context["request"].data["username"]
            )

            token, created = Token.objects.get_or_create(user=user)

            return Response(
                {
                    "success": True,
                    "message": "Login successfully",
                    "data": {
                        "user_id": user.pk,
                        "token": token.key,
                        "user_id": user.pk,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "is_active": user.is_active,
                        "fcm_token": user.profile.fcm_token,
                        "profie_photo_url": get_path(user.profile, request),
                    },
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": failure_error(serializer.errors),
                    "data": None,
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


def failure_error(ordered_errors):
    errors = []
    for x in ordered_errors.keys():
        errors.append(x)
    return ordered_errors.get(errors[0])[0]


def get_path(profile, request):

    if profile.image_url:
        return request.build_absolute_uri(profile.profie_photo_url.url)
    else:
        return None


class LogoutView(APIView):
    """ """

    def post(self, request, format=None):

        token = Token.objects.get(user=request.user)
        token.delete()

        return Response(
            {"success": True, "message": "successfully logout", "data": None},
            status=status.HTTP_200_OK,
        )
