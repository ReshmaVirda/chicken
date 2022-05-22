

from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from feed.models import  ProductFeed

class ProductFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeed
        fields = '__all__'
