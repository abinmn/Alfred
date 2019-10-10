from rest_framework import serializers
from api.models import *

class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'

class ExcelIdSerializer(serializers.ModelSerializer):
    college = serializers.StringRelatedField(many=False)

    class Meta:
        model = ExcelID
        fields = '__all__'
