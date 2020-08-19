from django.shortcuts import render
import operator
from django.http import HttpResponse 
def HomePage(requests):
    return HttpResponse('<h1>this is my home page</h1>')
def Aboutme(requests):
    return HttpResponse('I am Anvitha Vangala')
def Hobbies(requests):
    return HttpResponse('HOBBIES:Listening music,Browsing Net,Reading books,Watching Movies')
