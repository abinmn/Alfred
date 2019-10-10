from django.db import models

#List of Colleges
class College(models.Model):
    name = models.CharField(
        "College Name", max_length=200
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

    def __str__(self):
        return "%s - %s" % (self.id, self.name)

class Event(models.Model):
    id = models.CharField(primary_key = True, max_length=10)
    name = models.CharField("Event Name", max_length=50)
    rules = models.TextField("Event Rules", blank=True)
    venue = models.CharField(max_length = 100, blank=True)
    is_paid = models.BooleanField("Paid Event", default=False)
    is_team = models.BooleanField("Team Event", default=False)
    start_time = models.DateTimeField("Event Start Time", null=True, blank=True)
    end_time = models.DateTimeField("Event End Time", null=True, blank=True)
    base_price = models.IntegerField(default=0)
    mec_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Event_Participants(models.Model):
    event = models.ForeignKey(Event, verbose_name=("Event Id"), on_delete=models.CASCADE, related_name="participants")
    excel_id = models.ForeignKey(ExcelID, related_name="events", on_delete=models.CASCADE)
    #Applicable only for paid events
    have_paid = models.BooleanField()
    is_shortListed = models.BooleanField()
    is_winner = models.BooleanField()
    winner_position = models.IntegerField(blank=True, default=0)

    class Meta:
        verbose_name = "Event Participant"

    def __str__(self):
        return "%s - %s" % (self.event.name, self.excel_id.name)

class Team(models.Model):
    team_id = models.CharField(max_length=32)   
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="teams")
    members = models.ManyToManyField(ExcelID, related_name="teams")

    def __str__(self):
        return "%s %s" % (self.team_id, self.event.name)