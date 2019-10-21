import functools
from django.dispatch import receiver
from django.db.models.signals import post_save

from api.models import Team, Event_Participants
from api.helper_functions import misc

@receiver(post_save, sender=Team)
def create_participant_instance(sender, **kwargs):

    instance = kwargs.get("instance")
    team_members = instance.members.all()
    event = instance.event
    
    if kwargs.get("created"):
        participant_instance = map(
        functools.partial(misc.create_participant_instance, event=event),
        team_members
        )
        Event_Participants.objects.bulk_create(participant_instance)
    
    if not kwargs.get("created"):
        pass
