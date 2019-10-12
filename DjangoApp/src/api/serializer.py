from rest_framework import serializers
from api.models import *

class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'

class ExcelIdSerializer(serializers.ModelSerializer):
    college = serializers.SlugRelatedField(many=False, slug_field='name', queryset=College.objects.all())
    class Meta:
        model = ExcelID
        fields = '__all__'
