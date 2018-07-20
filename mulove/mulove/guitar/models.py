from django.db import models

class Instrument(models.Model):
    name = models.CharField(max_length=30)
    describtion = models.CharField(max_length=300)

# Create your models here.
