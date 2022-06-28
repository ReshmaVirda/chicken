from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from poultry_products.models import Governorate, Product, ProductName,ProductCate

class ProductSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    
    mobile_no = serializers.ReadOnlyField(source='creator.username')
    cate_name = serializers.ReadOnlyField(source='product_name.product_category.name')
    product_name_value = serializers.ReadOnlyField(source='product_name.name')
    product_category_id = serializers.ReadOnlyField(source='product_name.product_category.id')
    governorate_name  = serializers.ReadOnlyField(source='governorate.name')

    class Meta:
        model = Product
        fields = '__all__'

class ProductNameSerializer(serializers.ModelSerializer):
    cate_name = serializers.ReadOnlyField(source='product_category.name')
    
    class Meta:
        model = ProductName
        fields = '__all__'
        

class ProductCateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCate
        fields = '__all__'


class GovernorateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Governorate
        fields = '__all__'


