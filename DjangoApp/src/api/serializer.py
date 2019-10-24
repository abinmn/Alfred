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
        fields = ['id', 'name', 'logo']

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

class ParticipantEventSerializer(serializers.ModelSerializer):

    event= EventListSerializer(read_only=True)
    class Meta:
        model = Event_Participants
        fields = ['event']

class ParticipantDetailSerializer(serializers.ModelSerializer):

    personal_info = ExcelIdMinSerializer(source='excel_id', read_only=True)
    class Meta:
        model = Event_Participants
        fields = '__all__'

class ShortListSerializer(serializers.ModelSerializer):

    personal_info = ExcelIdMinSerializer(source='excel_id', read_only=True)
    class Meta:
        model = Event_Participants
        fields = ['excel_id', 'personal_info', 'is_shortListed']

class WinnerSerializer(serializers.ModelSerializer):
    personal_info = ExcelIdMinSerializer(source='excel_id', read_only=True)
    class Meta:
        model = Event_Participants
        fields = ['excel_id', 'personal_info', 'is_winner', 'winner_position']

class TeamSerializer(serializers.ModelSerializer):
    team_members = ExcelIdMinSerializer(source='members', many=True, read_only=True)
    
    class Meta:
        model = Team
        exclude = ['id']
        read_only_fields = ['team_id']
    