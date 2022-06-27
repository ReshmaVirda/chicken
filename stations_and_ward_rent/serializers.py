from rest_framework import serializers




from stations_and_ward_rent.models import StationAndWard

class StationAndWardSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    mobile_no = serializers.ReadOnlyField(source='creator.username')



    class Meta:
        model = StationAndWard
        fields = '__all__'
