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