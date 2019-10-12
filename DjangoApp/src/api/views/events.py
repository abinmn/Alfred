from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from api.serializer import *

class AllEventsList(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = EventListSerializer