from django.db import models

class Persons(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=45)
    credites = models.IntegerField()
    transactions = models.IntegerField(default=0)
