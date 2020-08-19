from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import operator

def Names(requests):
    return HttpResponse('This Phones Number,Home,Work,Friends,Unknown')
def Numbers(requests):
    return HttpResponse('Indian number consists of 10 digits with +91 as code')

