from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from mycontacts import views
urlpatterns = [
    url(r'Names.*', views.Names, name='Names'),
    url(r'Numbers.*', views.Numbers, name='Numbers'),
]
