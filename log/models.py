from django.db import models
from django.utils import timezone

#Create your models here.
class Donor(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	bloodType = models.CharField(max_length=10)
	createdDate = models.DateTimeField(default=timezone.now)

class Patient(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	blood_type = models.CharField(max_length=50)