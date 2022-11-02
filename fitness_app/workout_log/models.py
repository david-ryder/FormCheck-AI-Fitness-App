from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Exercise(models.Model):
    user_id = models.IntegerField()
    date = models.DateField('date performed')
    weight = models.IntegerField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    percent_success = models.FloatField()