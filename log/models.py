from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django import forms




#Create your models here.
class Donor(models.Model):
	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	bloodType = models.CharField(max_length=10)
	createdDate = models.DateTimeField(auto_now_add=True)
	lastAttendance = models.DateTimeField(auto_now_add=True)
	
class Patient(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	blood_type = models.CharField(max_length=50)
	created_date = models.DateTimeField(default=timezone.now)
	
