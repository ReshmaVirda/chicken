


from rest_framework import serializers
from feed.models import  ProductFeed

class ProductFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeed
        fields = '__all__'
