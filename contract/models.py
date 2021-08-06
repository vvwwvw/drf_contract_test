from django.db import models

# Create your models here.

class Contract(models.Model):
    title = models.CharField(max_length=200)
    contractor = models.CharField(max_length=200)
    departed = models.CharField(max_length=200)