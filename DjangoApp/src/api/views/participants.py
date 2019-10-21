from rest_framework import generics
from rest_framework import status


from api.helper_functions import baseviews, misc
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
        participant = ExcelID.objects.get(id=excel_id)
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
        return Team.objects.filter(event=event)
    
    def create(self, request, *args, **kwargs):
        members = request.data.get("members", [])
        event = misc.get_event(self)
        duplicate_team = misc.check_team_duplicate(members, event)
        if not duplicate_team:
            request.data["event"] = event.id
            return super().create(request, *args, **kwargs)
        
        #TODO: raise member in another team exception
    
    def partial_update(self, request, *args, **kwargs):

        return super().partial_update(request, *args, **kwargs)