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