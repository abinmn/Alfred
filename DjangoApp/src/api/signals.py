import functools
from django.dispatch import receiver
from django.db.models.signals import post_save, m2m_changed

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
        Event_Participants.objects.bulk_create(participant_instance)
    
