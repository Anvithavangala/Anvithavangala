
from django.http import HttpResponse
from django.shortcuts import render
import operator 
def HomePage(requests):
    return render(requests,'proj1/home.html')
def Aboutme(requests):
    return render(requests,'proj1/about.html')
def Hobbies(requests):
    return render(requests,'proj1/hobbies.html')