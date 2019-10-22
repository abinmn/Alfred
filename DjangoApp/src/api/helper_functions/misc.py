from functools import partial 
from api.models import *

from rest_framework import generics
from rest_framework import mixins
from rest_framework.exceptions import NotFound
from api.helper_functions import exceptions

def get_excel_id(excel_id):
	return ExcelID.objects.get(id=excel_id)

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

def get_event_participant(excel_id, event):
	try:
		participant = event.participants.get(excel_id=excel_id)
		return participant
	except:
		raise exceptions.custom('excel_id')

def create_participant_instance(excel_id, event):
	return Event_Participants(excel_id=excel_id, event=event)

def get_team(team_id):
	try:
		team = Team.objects.get(team_id=team_id)
		return team
	except:
		raise exceptions.custom('team_not_found')

def set_participant_status(participant, 
							shortlist_status=False, 
							is_winner=False, 
							winner_position=0):

	participant.is_shortListed = shortlist_status
	participant.is_winner = is_winner
	participant.winner_position = winner_position
	participant.save()

def set_team_status(team, query_params):
	is_shortListed = query_params.get('is_shortListed', False)    
	is_winner = query_params.get('is_winner', False)
	winner_position = query_params.get('winner_position', False)

	team.is_shortListed = is_shortListed
	team.is_winner = is_winner
	team.winner_position = winner_position
	team.save()



def get_excel_id(excel_id):
	try:
		return ExcelID.objects.get(id=excel_id)
	except:
		raise exceptions.custom("excel_id")


def check_team_duplicate(members, event):
	"""  
	Check if any member is part of another team for the same event
	"""
	members = map(get_excel_id, members)
	existing_team = Team.objects.filter(event=event, members__in=members).distinct().count()
	if existing_team == 0:
		return False
	return True