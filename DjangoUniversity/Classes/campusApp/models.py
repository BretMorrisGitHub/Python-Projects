from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campusName = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()

    #This makes the UniversityCampus objects display as the campus name
    def __str__(self):
        display_campus = '{0.campusName}'
        return display_campus.format(self)