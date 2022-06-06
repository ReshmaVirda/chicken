


from rest_framework import serializers
from feed.models import  ProductFeed

class ProductFeedSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()

    class Meta:
        model = ProductFeed
        fields = '__all__'
