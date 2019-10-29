from django.db import models
from api.helper_functions import generate
#List of Colleges
class College(models.Model):
    name = models.CharField(
        "College Name", max_length=200,
        unique=True
        )

    def __str__(self):
        return self.name

#TODO default price for excelid, events
class ExcelID(models.Model):
    id = models.CharField(primary_key = True, max_length=10)
    #references college table
    name = models.CharField("Student Name",max_length = 100)
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="students")
    email = models.EmailField("Email", max_length=254, unique=True)
    phone_number = models.IntegerField("Phone Number", unique=True)
    is_mecian = models.BooleanField(default=False)
    is_FullAccess = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    avatar = models.URLField(blank=True)


    def __str__(self):
        return "%s - %s" % (self.id, self.name)

class Event(models.Model):
    id = models.CharField(primary_key = True, max_length=10)
    name = models.CharField("Event Name", max_length=50)
    short_rules = models.TextField("Event Rules", blank=True)
    long_rules = models.TextField("Event Rules", blank=True)
    venue = models.CharField(max_length = 100, blank=True)
    is_paid = models.BooleanField("Paid Event", default=False)
    is_team = models.BooleanField("Team Event", default=False)
    is_active = models.BooleanField("Is Active", default=False)
    event_ended = models.BooleanField("Event Ended", default=False)
    start_time = models.DateTimeField("Event Start Time", null=True, blank=True)
    duration = models.DurationField("Event End Time", null=True, blank=True)
    base_price = models.IntegerField(default=0)
    mec_price = models.IntegerField(default=0)
    logo = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Event_Participants(models.Model):
    event = models.ForeignKey(Event, verbose_name=("Event Id"), on_delete=models.CASCADE, related_name="participants")
    excel_id = models.ForeignKey(ExcelID, related_name="events", on_delete=models.CASCADE)
    #Applicable only for paid events
    have_paid = models.BooleanField(default=False)
    is_shortListed = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    winner_position = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Event Participant"
        unique_together = [['excel_id','event']]

    def __str__(self):
        return "%s - %s" % (self.event.name, self.excel_id.name)

class Team(models.Model):
    team_id = models.CharField(max_length=32)   
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="teams")
    members = models.ManyToManyField(ExcelID, related_name="teams")
    is_shortListed = models.BooleanField(default=False)
    is_winner = models.BooleanField(default=False)
    winner_position = models.IntegerField(blank=True, default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.pk is None:
            self.team_id = generate.generate_team_id()
        return super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
    def __str__(self):
        return "%s %s" % (self.team_id, self.event.name)