#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    #donors
    url(r'^donors/$', views.donors,  name='donors'),
    #patients
    url(r'^patients/$', views.patients, name='patients')

]
