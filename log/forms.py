from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from . import models
from django.forms import ModelForm
from log.models import Donor


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

#add new donor
class PostForm(forms.ModelForm):
  firstName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), label='')
  lastName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), label='')
  blood_choices = (
            ('AB+','AB+'),
            ('AB-','AB-'),
            ('A+','A+'),
            ('A-','A-'),
            ('B+','B+'),
            ('B-','B-'),
            ('0+','0+'),
            ('0-','0-'),
            )
  # bloodType = forms.CharField(widget=forms.TextInput(max_length=200), label='', choices = blood_choices)
  bloodType = forms.ChoiceField(choices=blood_choices, widget=forms.Select(attrs={'class': 'form-control selectBlood'}),label='')
 #bloodType = forms.CharField(choices=blood_choices)

    #publisher = forms.MultipleChoiceField(widget=forms.SelectMultiple)
  class Meta:
    model = models.Donor

    fields = ['firstName', 'lastName', 'bloodType',]

# select type of blood
bloodChoices=[('select1','select 1'),
         ('select2','select 2')]

like = forms.ChoiceField(choices=bloodChoices, widget=forms.RadioSelect())


class PatientForm(forms.ModelForm):
  class Meta:
    model = models.Patient
    fields = ['first_name', 'last_name', 'blood_type',]


