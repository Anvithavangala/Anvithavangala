from django.shortcuts import render
from django.http import HttpResponse
import operator 
def home(requests):
    return render(requests,'proj/home.html')
def count(requests):
    text=requests.GET['full text']
    l=list(text.split())
    l1=[]
    for i in l:
        if [i,l.count(i)] not in l1:
            l1.append([i,l.count(i)])
    if(len(l1)==0):
        return HttpResponse("Please enter a valid string")
    else:
        return render(requests,'proj/frequency.html',{'yourlist':l1})
    

    
    