from rest_framework.exceptions import APIException

def custom(type):
    if type == 'excel_id':
        return APIException("Excel ID not found")
    
    if type == 'duplicate_team':
        return APIException("One or more member in another team")
    
    if type == 'team_not_found':
        return APIException("Invalid team_id")
    
    return APIException()