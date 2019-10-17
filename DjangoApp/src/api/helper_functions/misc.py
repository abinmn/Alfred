from api.models import *

from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import NotFound


def get_event_queryset(params):
	id = params.kwargs['id']
	event = Event.objects.filter(id=id)
	return event

def get_event(params):
	event_id = params.kwargs.get('id', None)
	event = Event.objects.get(id=event_id)
	return event
