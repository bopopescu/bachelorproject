#!python
#log/views.py
from django.utils import timezone  
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
from bson import json_util
from django.core.serializers.json import DjangoJSONEncoder
import json
from datetime import datetime
from django.utils import timezone
from datetime import date, timedelta
from django.utils.timesince import timesince
from datetime import datetime
from datetime import datetime, timedelta
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating


@login_required(login_url="login/")
def home(request):
    #display all the lates added donors
    query_results = Donor.objects.order_by('-createdDate')
    #dislay total ammount of rows
    donors_count = Donor.objects.count()

    # for item in query_results:
    #     item.blood = item.bloodType.count()

    return render(request,"home.html", {
        'donors_count': donors_count,
        'query_results': query_results,
        })

#donor
@login_required(login_url="login/")
def donors(request):
    global message
    if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()

    
    #display all the lates added donors
    query_results = Donor.objects.order_by('-createdDate')
    #dislay total ammount of rows
    donors_count = Donor.objects.count()

    delta = datetime.today() + timedelta(days=120)
    
    # loop attendance in database and add 4 months
    for item in query_results:
        item.dates = item.lastAttendance + timedelta(days=120)
        if item.dates >= datetime.now(tz=timezone.utc):
            item.message = "not available "

        else:
            item.message = "available"
            item.messageA = item.firstName 
   
    return render(request, 'donors.html', {
        'form': PostForm(), 
        'donors_count': donors_count,
        'query_results': query_results,
        'item': item,
        'item.message': item.message
        })

#patients
@login_required(login_url="login/")
def patients(request):
    if request.method == 'POST': # If the form has been submitted...
        form2 = PatientForm(request.POST) # A form bound to the POST data
        if form2.is_valid():
            form2.save()

    patients_results = Patient.objects.all()
    patients_count = Patient.objects.count()
    return render(request, 'patients.html', {
        'form2': PatientForm(), 
        'patients_results': patients_results,
        'patients_count': patients_count,
        })


