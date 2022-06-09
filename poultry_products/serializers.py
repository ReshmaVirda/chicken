from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from poultry_products.models import Region, Governorate, Product, ProductName

class ProductSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    last_name = serializers.ReadOnlyField(source='creator.last_name')


    class Meta:
        model = Product
        fields = '__all__'

class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = '__all__'
        
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'


