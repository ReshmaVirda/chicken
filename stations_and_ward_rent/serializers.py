from rest_framework import serializers




from stations_and_ward_rent.models import StationAndWard

class StationAndWardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StationAndWard
        fields = '__all__'
