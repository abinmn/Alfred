from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from api.helper_functions import misc

class ParticipantListCreateUpdateAPIView(generics.ListCreateAPIView,
                                        generics.UpdateAPIView, 
                                        generics.DestroyAPIView):
    """  
    A base class to deal with Event_Participant table
    """
    def partial_update(self, request, *args, **kwargs):
        self.request.data["event"] = kwargs.get("id", None)
        return self.update(request, *args, **kwargs)
    
    def get_object(self):
        event = misc.get_event(self)
        excel_id = self.request.data.get("excel_id", None)
        return misc.get_event_participant(event, excel_id)
       

class ParticipantUpdateWithList(generics.UpdateAPIView):
   
    def create(self, request, *args, **kwargs):
        event = misc.get_event(self)
        data = self.request.data

        """  
        """
        if isinstance(data, list):
            for excel_id in data:
                participant = misc.get_event_participant(event, excel_id)
                misc.set_participant_status(participant, shortlist_status=True)
            return self.get(request, *args, *kwargs)         

        if isinstance(data, dict):
            """  
            Create from a single request
            """
            excel_id = data.get("excel_id", None)

            shortlist_status = data.get("is_shortListed", False)
            winner = data.get("is_winner", False)
            winner_position = data.get("winner_position", 0)

            participant = misc.get_event_participant(event, excel_id)
            misc.set_participant_status(participant, shortlist_status, winner, winner_position)            
            return self.update(request, *args, *kwargs)