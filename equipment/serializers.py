from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from equipment.models import  ProductEquipment

class ProductEquipmentSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    mobile_no = serializers.ReadOnlyField(source='creator.username')
    governorate_name  = serializers.ReadOnlyField(source='governorate.name')
    class Meta:
        model = ProductEquipment
        fields = '__all__'
