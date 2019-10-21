import uuid
from django.core.exceptions import ObjectDoesNotExist

from api.models import ExcelID, Team
import pyqrcode

def generate_id():
    last_id = ExcelID.objects.latest('id').id
    last_id_alpha = last_id[:2]
    last_id_num = int(last_id[2:])

    new_id = last_id_num + 1
    new_id = last_id_alpha + str(new_id)

    try:
        instance = ExcelID.objects.get(id=new_id)
        assert instance == None, "Can't generate id"
    except ObjectDoesNotExist:
        return new_id

def generate_qr(excel_id):
    qr = pyqrcode.create(excel_id)
    return qr

def generate_team_id():
    team_id = uuid.uuid4().hex
    try:
        team = Team.objects.get(team_id=team_id)
        return generate_team_id()
    except ObjectDoesNotExist:
        return team_id