from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from api.serializer import *
from api.helper_functions import misc


class AllEventsList(ListAPIView):
    """ 
    Get: Returns a list of all events
    """
    queryset = Event.objects.all()
    serializer_class = EventListSerializer

class PaidEventsList(ListAPIView):
    """ 
    Get: Returns a list of all paid events
    """
    queryset = Event.objects.filter(is_paid=True)
    serializer_class = EventListSerializer

class EventDetails(RetrieveAPIView):
    """  
    Get: Returns the details of an event with short_rules
    """
    serializer_class = EventDetailsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return misc.get_event_queryset(self)

class EventRules(RetrieveAPIView):
    """  
    Get: Returns the event rules
    """
    serializer_class = EventRulesSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return misc.get_event_queryset(self)

class EventStatus(RetrieveUpdateAPIView):
    """  
    PATCH: Update whether event has started or not
    """
    serializer_class = EventStatusSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return misc.get_event_queryset(self)
        