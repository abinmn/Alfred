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
    