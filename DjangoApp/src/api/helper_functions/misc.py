from functools import partial 
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
	try:
		event = Event.objects.get(id=event_id)
		return event
	except:
		raise NotFound

def get_event_participant(event, excel_id):
	try:
		participant = event.participants.get(excel_id=excel_id)
		return participant
	except:
		raise NotFound

def set_participant_status(participant, 
							shortlist_status=False, 
							is_winner=False, 
							winner_position=0):

	participant.is_shortListed = shortlist_status
	participant.is_winner = True
	participant.winner_position = winner_position
	participant.save()

def create_participant_instance(excel_id, event):
	return Event_Participants(excel_id=excel_id, event=event)