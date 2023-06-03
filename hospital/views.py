from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from hospital import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
#query ar jonno
from django.db.models import Q

#django.db.model all item need for use
from django.db.models import Avg, Max, Min, Count
#from numpy import product

#google map ar jonno
#from __future__ import division
from multiprocessing import context
from turtle import color
from unittest import result
from django.db.models import Q
import json
# all models and forms name add korar jonno * use kora jay
from .models import *
from .forms import *

# Create your views here.
def doctorformfill(request):
    form=DoctorDetailsForm()
     
    if request.method == "POST":
        form=DoctorDetailsForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, 'Thank you')
    context={'form':form}

    return render(request, 'index.html', context)

####### AutoSearch API ######..work
def auto_house(request):
    if request.is_ajax():
        q = request.GET.get('term')
        places = DoctorDetails.objects.filter(area__icontains=q)
        results = []
        for pl in places:
            place_json = {}
            place_json = pl.area
            results.append(place_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)



#AUTO query not min max query.So use POST method.If min max then use GET method
 
def details(request):
              
        doclist=DoctorDetails()
        doclist=DoctorDetails.objects.all().order_by('name')
      
        return render(request, 'details.html',{'doclist':doclist})
     
        

def testsearch(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        queryx=request.GET.get('queryx')
        queryday=request.GET.get('queryday')

        if query and queryx and queryday:
            products = DoctorDetails.objects.filter(area__icontains=query,special__icontains=queryx, daywork__icontains=queryday).order_by('name') 
            return render(request, 'testsearch.html', {'products':products})
        elif query and queryx or queryday:
            products = DoctorDetails.objects.filter(area__icontains=query,special__icontains=queryx,daywork__icontains=queryday).order_by('name') 
            return render(request, 'testsearch.html', {'products':products})
        elif query or queryx and queryday:
            products = DoctorDetails.objects.filter(area__icontains=query,special__icontains=queryx,daywork__icontains=queryday).order_by('name') 
            return render(request, 'testsearch.html', {'products':products})
        elif query:
            products = DoctorDetails.objects.filter(area__icontains=query,special__icontains=queryx,daywork__icontains=queryday).order_by('name') 
            return render(request, 'testsearch.html', {'products':products})
        elif queryx:
            products = DoctorDetails.objects.filter(area__icontains=query,special__icontains=queryx,daywork__icontains=queryday).order_by('name') 
            return render(request, 'testsearch.html', {'products':products})
        elif queryday:
            products = DoctorDetails.objects.filter(area__icontains=query,special__icontains=queryx,daywork__icontains=queryday).order_by('name') 
            return render(request, 'testsearch.html', {'products':products})
        else:
            print("No information to show")
            return render(request, 'testsearch.html', {})
        
