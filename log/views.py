#!python
#log/views.py
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
       # 'query_results': query_results,
        'donors_count': donors_count,
        'query_results': query_results,
       # 'filter': donor_filter,

        })




@login_required(login_url="login/")
def patients(request):
    if request.method == 'POST': # If the form has been submitted...
        form = PatientForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            form.save()

    patients_results = Patient.objects.all()
    return render(request, 'patients.html', {'form': PatientForm(), 'patients_results': patients_results})

# def post_new(request):
#     form = PostForm()
#     return render(request, 'log/p.html', {'form': form})



