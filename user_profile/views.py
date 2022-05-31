from django.shortcuts import render
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from user_profile.models import Profile
from user_profile.serializers import RegisterSerializer, ProfileSerializer
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
                        "profile_photo_url": get_path(user.profile, request),
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
        return request.build_absolute_uri(profile.profile_photo_url.url)
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


class RegisterView(ObtainAuthToken,APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user_obj = User.objects.create(
                    username=request.data["mobile_no"],
                    email=request.data.get("mobile_no"),
                    first_name=request.data.get("first_name"),
                    last_name=request.data.get("last_name"),
                )
                request.data["username"] = request.data["mobile_no"]
                
                user_obj.set_password(request.data["password"])
                user_obj.save()
                profile = Profile.objects.create(
                    user=user_obj,
                    is_registred=True,
                )

                serializer = self.serializer_class(
                    data=request.data, context={"request": request}
                )
                serializer.is_valid(raise_exception=True)

                token, created = Token.objects.get_or_create(user=user_obj)


                return Response(
                    {
                        "success": True,
                        "message": "User Registered Successfully",
                        "data": {
                            "token": token.key,

                            "user_id": user_obj.pk,
                            "first_name": user_obj.first_name,
                            "last_name": user_obj.last_name,
                            "is_active": user_obj.is_active,
                            "is_registred": profile.is_registred,
                            "fcm_token": profile.fcm_token,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
            except:
                return Response(
                    {
                        "success": False,
                        "message": "user already exists with same mobile no ",
                        "data": None,
                        "errors": "user already exists with same mobile no ",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
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


class UserAPIView(APIView):
    """
    ME API
    """

    def get(self, request, format=None):

        user = request.user

        return Response(
            {
                "success": True,
                "message": "data retrieved",
                "data": {
                    "user_id": user.pk,
                    
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "is_active": user.is_active,
                    
                    # "is_registred": request.user.profile.is_registred,
                    "fcm_token": request.user.profile.fcm_token,
                    "profile_photo_url": get_path(request.user.profile, request),
                    "role": request.user.profile.role,
                    "mobile_no": request.user.username,
                },
            },
            status=status.HTTP_200_OK,
        )
from rest_framework import parsers

class FileUploadView(APIView):
    permission_classes = []
    parser_class = (parsers.FileUploadParser,)

    def post(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)
        file_serializer = ProfileSerializer(profile, data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            
            return Response(
                {
                    "success": True,
                    "message": "profile photo uploaded",
                    "data": {
                        "profile_photo_url": get_path(request.user.profile, request),
                    },
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": str(failure_error(file_serializer.errors)),
                    "data": None,
                    "errors": file_serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )