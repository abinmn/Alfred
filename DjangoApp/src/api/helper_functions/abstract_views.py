from rest_framework import generics
from api.helper_functions import misc

class ParticipantListCreateUpdateAPIView(generics.ListCreateAPIView, generics.UpdateAPIView):
    """  
    A base class to deal with Event_Participant table
    """
    def partial_update(self, request, *args, **kwargs):
        self.request.data["event"] = kwargs.get("id", None)
        return self.update(request, *args, **kwargs)
    
    def get_object(self):
        event = misc.get_event(self)
        excel_id = self.request.data.get("excel_id", None)
        participant = event.participants.get(excel_id=excel_id)
        return participant

    def get_queryset(self):
        event = misc.get_event(self)
        participants = event.participants.all()
        return participants