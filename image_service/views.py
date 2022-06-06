from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from user_profile.models import Profile
from image_service.serializers import ImageFileSerializer
from django.conf import settings
from rest_framework import parsers
from poultry_products.views import failure_error


class FileUploadView(APIView):

    parser_class = parsers.FileUploadParser

    def post(self, request, *args, **kwargs):

        file_serializer = ImageFileSerializer(data=request.data)
        if file_serializer.is_valid():
            obj = file_serializer.save()

            return Response(
                {
                    "success": True,
                    
                    "message": "profile photo uploaded",
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
