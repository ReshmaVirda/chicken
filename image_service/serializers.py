from rest_framework import serializers
from poultry_products.models import ImageFile
class ImageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFile
        fields = fields = ("file_url","id")


