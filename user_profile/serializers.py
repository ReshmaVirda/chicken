from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from user_profile.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "groups", "first_name", "last_name", "is_active"]


class RegisterSerializer(serializers.Serializer):

    mobile_no = serializers.CharField(required=False)
    fcm_token = serializers.CharField(required=False)

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )

    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        fields = (
            "fcm_token",
            "mobile_no",
            "password",
            "first_name",
            "last_name",
        )
