from rest_framework import serializers
from veterinary_medicine.models import VeterinaryMadicine

class VeterinaryMadicineSerializer(serializers.ModelSerializer):
    get_image_url = serializers.ReadOnlyField()

    class Meta:
        model = VeterinaryMadicine
        fields = '__all__'
