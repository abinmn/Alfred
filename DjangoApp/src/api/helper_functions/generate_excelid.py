from django.core.exceptions import ObjectDoesNotExist

from api.models import ExcelID as EID

def generate():
    last_id = EID.objects.latest('id').id
    last_id_alpha = last_id[:2]
    last_id_num = int(last_id[2:])

    new_id = last_id_num + 1
    new_id = last_id_alpha + str(new_id)

    try:
        instance = EID.objects.get(id=new_id)
        assert instance == None, "Can't generate id"
    except ObjectDoesNotExist:
        return new_id