from rest_framework import serializers
from veterinary_medicine.models import VeterinaryMadicine

class VeterinaryMadicineSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    mobile_no = serializers.ReadOnlyField(source='creator.username')
    governorate_name  = serializers.ReadOnlyField(source='governorate.name')
    class Meta:
        model = VeterinaryMadicine
        fields = '__all__'
