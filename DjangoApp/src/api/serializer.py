from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import *

class CollegeSerializer(serializers.ModelSerializer):

    class Meta:
        model = College
        fields = '__all__'

class ExcelIdSerializer(serializers.ModelSerializer):
    college = serializers.SlugRelatedField(many=False, slug_field='name', 
                                        queryset=College.objects.all())
    
    class Meta:
        model = ExcelID
        fields = '__all__'

class ExcelIdMinSerializer(serializers.ModelSerializer):
    college = serializers.SlugRelatedField(many=False, slug_field='name', queryset=College.objects.all())
    class Meta:
        model = ExcelID
        fields = ['id', 'name', 'college']

class EventListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name']

class EventDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        exclude = ['long_rules']

class EventRulesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'name','short_rules', 'long_rules']

class EventStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ['id', 'is_active']

class ParticipantDetailSerializer(serializers.ModelSerializer):

    personal_info = ExcelIdMinSerializer(source='excel_id', read_only=True)
    class Meta:
        model = Event_Participants
        fields = '__all__'
    