from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import parsers
from user_profile.models import Profile, User
from user_profile.serializers import RegisterSerializer, ProfileSerializer, UpdateUserSerializer


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
                        "first_name": user.first_name,
                        "last_name":user.last_name,
                        "address":user.address,
                        "location":user.location,
                        "country_code":user.country_code,
                        "is_active": user.is_active,
                        "is_registred": request.user.profile.is_registred,
                        "fcm_token": user.profile.fcm_token,
                        "profile_photo_url": user.profile.image_url,
                        "role": request.user.profile.role,
                        "mobile_no": request.user.mobile_no,
                        "username": request.user.mobile_no, 
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
        serializer = User.objects.filter(mobile_no=request.data["mobile_no"])
        if len(serializer) > 0:
            return Response({ "success": False,
                    "message": "User Already Exist With This Mobile."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            location = ""
            address = ""
            if 'location' in request.data:
                location = request.data.get("location")
            

            if 'address' in request.data:
                address = request.data.get("address")

            user_obj = User.objects.create(
                mobile_no=request.data["mobile_no"],
                first_name=request.data.get("first_name"),
                last_name=request.data.get("last_name"),
                country_code=request.data.get("country_code"),
                location=location,
                address=address
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
                        "user_id": user_obj.pk,
                        'username':user_obj.mobile_no,
                        'mobile':user_obj.mobile_no,
                        "first_name": user_obj.first_name,
                        "last_name":user_obj.last_name,
                        "country_code":user_obj.country_code,
                        "location":user_obj.location,
                        "address":user_obj.address,
                        "token": token.key,
                        "is_active": user_obj.is_active,
                        "is_registred": profile.is_registred,
                        "fcm_token": profile.fcm_token,
                        "profile_photo_url":None
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
                    "country_code":user.country_code,
                    "mobile_no":user.mobile_no,
                    "username":user.mobile_no,
                    "location":user.location,
                    "address":user.address,
                    "is_active": user.is_active,
                    "is_registred": request.user.profile.is_registred,
                    "fcm_token": request.user.profile.fcm_token,
                    "profile_photo_url": request.user.profile.image_url,
                    "role": request.user.profile.role
                },
            },
            status=status.HTTP_200_OK,
        )

class FileUploadView(APIView):

    parser_class = (parsers.FileUploadParser,)

    # def post(self, request, *args, **kwargs):
    #     profile = Profile.objects.get(user=request.user)

    #     file_serializer = ProfileSerializer(profile, data=request.data)
    #     if file_serializer.is_valid():
    #         profile =file_serializer.save()
            
    #         return Response(
    #             {
    #                 "success": True,
    #                 "message": "profile photo uploaded",
    #                 "data": {
    #                     "profile_photo_url": profile.image_url,
    #                 },
    #             },
    #             status=status.HTTP_200_OK,
    #         )

    #     else:
    #         return Response(
    #             {
    #                 "success": False,
    #                 "message": str(failure_error(file_serializer.errors)),
    #                 "data": None,
    #                 "errors": file_serializer.errors,
    #             },
    #             status=status.HTTP_400_BAD_REQUEST,
    #         )

    def put(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        file_serializer = ProfileSerializer(profile, data=request.data)
        if file_serializer.is_valid():
            profile =file_serializer.save()
            if 'profile_photo_url' in request.data:
                return Response(
                    {
                        "success": True,
                        "message": "profile photo uploaded",
                        "data": {
                            "profile_photo_url": profile.image_url,
                        },
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "success": True,
                        "message": "profile update successfully",
                        "data": file_serializer.data,
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
    


class ForgotPasswordRequest(APIView):
    """ """
    permission_classes = (AllowAny,)
    def post(self, request, format=None):

        return Response(
            {
                "success": True,
                "message": "Sent OTP successfully",
                "data": {"otp": 1234},
            },
            status=status.HTTP_200_OK,
        )


class ForgotPasswordView(APIView):

    """
    user create
    """

    permission_classes = (AllowAny,)

    def post(self, request, format=None):


        try:
            user = User.objects.get(username=request.data["mobile_no"])
            if request.data["otp"]!=user.profile.otp:
                raise Exception
            user.set_password(request.data["password"])
            user.save()
            return Response(
                {
                    "success": True,
                    "message": "Password changed successfully.",
                    "data": [],
                },
                status=status.HTTP_200_OK,
            )

        except  Exception as e:

            return Response(
                {
                    "success": False,
                    "message": "Please add password",
                    "data": None,
                    "errors": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

class UpdateView(APIView):
    """ """
    def put(self, request, format=None):
        
        serializer = UpdateUserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                {
                    "success": True,
                    "message": "Profile Updated",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {
                    "success": False,
                    "message": str(failure_error(serializer.errors)),
                    "data": None,
                    "errors": serializer.errors,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
