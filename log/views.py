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
import datetime
from bson import json_util
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.core.files.storage import FileSystemStorage



# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating


@login_required(login_url="login/")
def home(request):
	return render(request,"home.html")

#donor
@login_required(login_url="login/")
def donors(request):
    global message
    if request.method == 'POST':
        if 'saveDonor' in request.POST:
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()

        

        elif 'attend' in request.POST:
            donor_id = None
            # if request.method == "GET":
            #     donor_id = request.GET.get('id')

            if donor_id:
                donor = Donor.objects.get(id=int(donor_id))
                if donor:
                    donor.lastAttendance.add(datetime.datetime.now())
                    donor.save()
                

        # elif 'uploadImg' in request.FILES['myfile']:
        #     myfile = request.FILES['myfile']
        #     fs = FileSystemStorage()
        #     filename = fs.save(myfile.name, myfile)
        #     uploaded_file_url = fs.url(filename)

            # selecting file and saving in the folder
        elif 'uploadImg' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
    
    

    #display all the lates added donors
    query_results = Donor.objects.order_by('-createdDate')
    #dislay total ammount of rows
    donors_count = Donor.objects.count()
   
    return render(request, 'donors.html', {
        'form': PostForm(), 
        'donors_count': donors_count,
        'query_results': query_results,
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


