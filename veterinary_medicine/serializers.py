from rest_framework import serializers
from veterinary_medicine.models import VeterinaryMadicine

class VeterinaryMadicineSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()
    first_name = serializers.ReadOnlyField(source='creator.first_name')
    last_name = serializers.ReadOnlyField(source='creator.last_name')


    class Meta:
        model = VeterinaryMadicine
        fields = '__all__'
