#!python
# log/urls.py
from django.conf.urls import url
from . import views

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
# from uploads.core import views

# from .views import get_data

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    #donors
    url(r'^donors/$', views.donors,  name='donors'),
	# url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),    #patients
    url(r'^patients/$', views.patients, name='patients')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
