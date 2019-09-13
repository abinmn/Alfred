from django.db import models

#List of Colleges
class College(models.Model):
    college = models.CharField("College Name", max_length=200)

    def __str__(self):
        return self.college

#TODO default price for excelid, events
class ExcelID(models.Model):
    id = models.CharField(primary_key = True, max_length=10)
    #references college table
    name = models.CharField("Student Name",max_length = 100)
    college = models.OneToOneField(College, on_delete=models.CASCADE)
    email = models.EmailField("Email", max_length=254)
    phone_number = models.IntegerField("Phone Number")
    is_mecian = models.BooleanField(default=False)
    price = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.excel_id, self.excel_id.name)

class Event(models.Model):
    id = models.CharField(primary_key = True, max_length=10)
    name = models.CharField("Event Name", max_length=50)
    rules = models.TextField("Event Rules")
    venue = models.CharField(max_length = 100)
    is_paid = models.BooleanField("Paid Event", default=False)
    is_team = models.BooleanField("Team Event", default=False)
    start_time = models.DateTimeField("Event Start Time", auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField("Event End Time", auto_now=False, auto_now_add=False)
    base_price = models.IntegerField()
    mec_price = models.IntegerField()

    def __str__(self):
        return self.name

class Event_Participants(models.Model):
    event = models.ManyToManyField(Event, verbose_name=("Event Id"), related_name="event")
    excel_id = models.ManyToManyField(ExcelID, related_name="excelID")
    #Applicable only for paid events
    have_paid = models.BooleanField()
    is_shortListed = models.BooleanField()
    is_winner = models.BooleanField()
    winner_position = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.excel_id, self.excel_id.name)

class Team(models.Model):
    team_id = models.CharField(max_length=32)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    excel_id = models.ManyToManyField(ExcelID, related_name="student")

    def __str__(self):
        return "%s %s %s" % (self.team_id, self.event.name, self.excel_id.name)