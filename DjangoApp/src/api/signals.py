import functools
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed
from django.db import IntegrityError
from django.db import transaction


from api.models import Team, Event_Participants
from api.helper_functions import misc

@receiver(m2m_changed, sender=Team.members.through)
def create_participant_instance(sender, **kwargs):

    instance = kwargs.get("instance")
    team_members = instance.members.all()
    event = instance.event
    if kwargs.get("action") == 'post_add':
        participant_instance = map(
            functools.partial(misc.create_participant_instance, event=event),
            team_members
        )
        try:
            with transaction.atomic():
                participants = Event_Participants.objects.bulk_create(participant_instance)
                instance.members.set(team_members)
        except IntegrityError:
            pass
  
    
@receiver(post_save, sender=Team)
def update_participant_instance(sender, **kwargs):
    instance = kwargs.get("instance")
    team_members = instance.members.all()
    event = instance.event

    participant_instance = Event_Participants.objects.filter(
        event = event,
        excel_id__in = team_members
    )
    participant_instance.update(
        is_shortListed = instance.is_shortListed,
        is_winner = instance.is_winner,
        winner_position = instance.winner_position
    )