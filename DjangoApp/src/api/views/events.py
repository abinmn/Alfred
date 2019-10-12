from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from api.serializer import *

class AllEventsList(ListAPIView):
    """ 
    Get: Returns a list of all events
    """
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

class EventDetails(RetrieveAPIView):
    """  
    Get: Returns the details of an event with short_rules
    """
    serializer_class = EventDetailsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        event = Event.objects.filter(id=id)
        return event

class EventRules(RetrieveAPIView):

    serializer_class = EventRulesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        id = self.kwargs['id']
        event = Event.objects.filter(id=id)
        return event
