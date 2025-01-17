import uuid
from django.core.exceptions import ObjectDoesNotExist

from api import models

def generate_id():
    try:
        last_id = models.ExcelID.objects.latest('id').id
        last_id_alpha = last_id[:2]
        last_id_num = int(last_id[2:])
    except:
        last_id_alpha = 'EX'
        last_id_num = 0
        
    new_id = last_id_num + 1
    new_id = last_id_alpha + str(new_id)

    try:
        instance = models.ExcelID.objects.get(id=new_id)
        assert instance == None, "Can't generate id"
    except ObjectDoesNotExist:
        return new_id


def generate_team_id():
    team_id = uuid.uuid4().hex
    try:
        team = models.Team.objects.get(team_id=team_id)
        return generate_team_id()
    except ObjectDoesNotExist:
        return team_id

def generate_pin():
    pin = int(str(uuid.uuid4().int)[:6])
    return pin