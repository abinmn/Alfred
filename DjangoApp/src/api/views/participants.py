from rest_framework import generics
from rest_framework import status

from api.helper_functions import baseviews, misc, exceptions
from api.serializer import *
from api import models

class ParticipantsDetailsView(baseviews.ParticipantListCreateUpdateAPIView):
    
    serializer_class = ParticipantDetailSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event = misc.get_event(self)
        return event.participants.all()
        

class ShortListView(baseviews.ParticipantUpdateWithList,
                    baseviews.ParticipantListCreateUpdateAPIView):

    serializer_class = ShortListSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event = misc.get_event(self)
        return event.participants.filter(is_shortListed=True)

class WinnersView(baseviews.ParticipantUpdateWithList,
                baseviews.ParticipantListCreateUpdateAPIView):
    
    serializer_class = WinnerSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event = misc.get_event(self)
        return event.participants.filter(is_winner=True)

class ExcelIDEventsView(generics.ListAPIView):
    serializer_class = ParticipantEventSerializer

    def get_queryset(self):
        excel_id = self.request.query_params.get('excel_id', None)
        participant = misc.get_excel_id(excel_id)
        events = participant.events.all().prefetch_related('event')
        return events
    
class SpecificEventsExcelIDView(generics.RetrieveAPIView):
    serializer_class = ParticipantDetailSerializer
    lookup_field = 'id'

    def get_object(self):
        queryset = self.get_queryset()
        return queryset.first()

    def get_queryset(self):
        excel_id = self.request.query_params.get('excel_id', None)
        event = misc.get_event(self)
        return event.participants.filter(excel_id=excel_id)
    
class TeamDetailsViews(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = TeamSerializer
    lookup_field = 'id'

    def get_queryset(self):
        event = misc.get_event(self)

        excel_id = self.request.query_params.get('excel_id', None)    
        is_shortListed = self.request.query_params.get('is_shortListed', False)    
        is_winner = self.request.query_params.get('is_winner', False)    

        #return excel_id's team for particular event
        if excel_id:
            excel_id = misc.get_excel_id(excel_id)
            event = misc.get_event(self)
            return excel_id.teams.filter(event=event)
        
        if is_shortListed:
            return Team.objects.filter(event = event, is_shortListed = is_shortListed)

        if is_winner:
            return Team.objects.filter(event = event, is_winner = is_winner)                        
        
        return Team.objects.filter(event = event)
    
    def get_object(self):
        try:
            team_id = self.request.data.get("team_id", None)
            team = misc.get_team(team_id)
            return team
        except:
            pass  

    def create(self, request, *args, **kwargs):
        members = request.data.get("members", [])
        event = misc.get_event(self)
        duplicate_team = misc.check_team_duplicate(members, event)
        
        if not duplicate_team:
            request.data["event"] = event.id
            return super().create(request, *args, **kwargs)
        
        raise exceptions.custom('duplicate_team')
    
    def partial_update(self, request, *args, **kwargs):
        data = request.data
        if isinstance(data, list):
            for team in data:
                team_id = team.get("team_id")
                team_instance = misc.get_team(team_id)
                misc.set_team_status(team_instance, team)
            return self.get(request, *args, **kwargs)

        return super().partial_update(request, *args, **kwargs)