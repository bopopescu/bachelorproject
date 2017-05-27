#!python
#log/views.py
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from log.forms import PostForm
from log.models import Donor
from log.models import Patient
from log.forms import PatientForm
# from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .filters import DonorFilter
from log.tables import PersonTable

# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating


@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

@login_required(login_url="login/")
def donors(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PostForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save() 

    #display all donors
    query_results = Donor.objects.all()
    #dislay total ammount of rows
    donors_count = Donor.objects.count()

    return render(request, 'donors.html', {
        'form': PostForm(), 
        'donors_count': donors_count,
        'query_results': query_results,
        })

def get_data(request):
    data = {
    'sales': 100,
    'customers': 30
    }



    return JsonResponse(data) # http response

@login_required(login_url="login/")
def patients(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PatientForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()

    patients_results = Patient.objects.all()
    patients_count = Patient.objects.count()
    return render(request, 'patients.html', {
        'form': PatientForm(), 
        'patients_results': patients_results,
        'patients_count': patients_count,
        })


