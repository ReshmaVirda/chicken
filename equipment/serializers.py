from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers



from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from equipment.models import  ProductEquipment

class ProductEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEquipment
        fields = '__all__'
