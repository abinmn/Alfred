from api.models import *

from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import NotFound


def get_event_queryset(params):
		id = params.kwargs['id']
		event = Event.objects.filter(id=id)
		return event