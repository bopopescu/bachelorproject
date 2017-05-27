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
  bloodType = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Blood Type'}), label='') 
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


