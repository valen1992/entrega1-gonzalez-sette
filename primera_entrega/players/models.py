from django.db import models

# Create your models here.

class Players(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()

class Clubs(models.Model):
    name = models.CharField(max_length=50)
    country = models.FloatField()

class Tecnicos(models.Model):
    name = models.CharField(max_length=50)
    experience = models.FloatField()