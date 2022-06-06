from rest_framework import serializers




from stations_and_ward_rent.models import StationAndWard

class StationAndWardSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()

    class Meta:
        model = StationAndWard
        fields = '__all__'
