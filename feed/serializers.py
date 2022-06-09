


from rest_framework import serializers
from feed.models import  ProductFeed

class ProductFeedSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    last_name = serializers.ReadOnlyField(source='creator.last_name')


    class Meta:
        model = ProductFeed
        fields = '__all__'
