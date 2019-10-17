from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from api.helper_functions import abstract_views, misc
from api.serializer import *
from api import models

class ParticipantsDetailsView(abstract_views.ParticipantListCreateUpdateAPIView):
    
    serializer_class = ParticipantDetailSerializer
    lookup_field = 'id'

    