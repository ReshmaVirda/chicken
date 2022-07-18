from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from user_profile.models import Profile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', "first_name", "last_name", "mobile_no", 'location', 'address', 'country_code', "is_active", 'is_admin']
        extra_kwargs = {
            'id':{"read_only":True},
            'is_active':{"read_only":True},
            'is_admin':{"read_only":True}
        }

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", 'location', 'address']

    extra_kwargs ={
        "first_name":{"required":False},
        "last_name":{"required":False},
        "mobile_no":{"required":False},
        'location':{"required":False},
        'address':{"required":False},
        'country_code':{"required":False}
    }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = fields = ("profile_photo_url","id", "fcm_token", "role")
    
    extra_kwargs ={
        "fcm_token":{"required":False},
        "role":{"required":False},
        "profile_photo_url":{"required":False}
    }


class RegisterSerializer(serializers.Serializer):

    mobile_no = serializers.CharField(required=True)
    location = serializers.CharField(required=False)
    address = serializers.CharField(required=False)

    fcm_token = serializers.CharField(required=False)

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    country_code = serializers.CharField(required=True)

    class Meta:
        fields = (
            "fcm_token",
            "mobile_no",
            "password",
            "first_name",
            "last_name",
            "location",
            "address",
            "country_code"
        )
