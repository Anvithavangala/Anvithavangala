from django.http import HttpResponse
from django.shortcuts import render
import operator
def HomePage(requests):
   return render(requests,'app1/home.html',{'username':'Anvitha'})
def Aboutme(requests):
   return render(requests,'app1/about.html',{'userid':'Anvitha30'})
def Hobbies(requests):
   return render(requests,'app1/hobbies.html',{'userid':'Anvitha30'})