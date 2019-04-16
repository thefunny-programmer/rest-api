from django.db import models
import datetime


class Patient(models.Model):

    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    problem = models.CharField(max_length = 200)
    entry_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name