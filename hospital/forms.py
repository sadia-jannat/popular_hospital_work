import django
from django.contrib.auth import models
from django.core import validators
from django import forms
from django.forms import fields, widgets
from django import forms

#models
from .models import *


class DoctorDetailsForm(forms.ModelForm):
    class Meta:
        model=DoctorDetails
        fields=['name', 'email', 'phone', 'nid', 'area',  'special','daywork']
        labels={'name':'Enter your name', 'email':'Enter you email' ,
                'phone':'Enter your phone','nid':'Enter your NID number',
                'area':'Your hospital location',  'special':'Your speciality',
                'daywork':'Day name'}
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'nid': forms.NumberInput(attrs={'class':'form-control'}),
            'area': forms.Select(attrs={'class':'form-select'}),
            'special': forms.Select(attrs={'class':'form-select'}),
            'daywork': forms.Select(attrs={'class':'form-select'}),
        }

#query for search
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)   
    #querycategory=forms.CharField(max_length=100)
    #queryday=forms.CharField(max_length=100) 

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['doctor_name','name', 'phone', 'email', 'location', 'patient_category',  'details']
        labels={'doctor_name':'Enter doctor name', 'name':'Enter your name', 'phone':'Enter your phone','email':'Enter you email',
                'location':'Your location', 'patient_category':'Are you New patient?',
                'details':'Enter your some details of diseases history'}
        widgets={
            'doctor_name':forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'patient_category': forms.Select(attrs={'class':'form-select'}),
            'details': forms.TextInput(attrs={'class':'form-control'}),
        }
