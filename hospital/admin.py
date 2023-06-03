from django.contrib import admin

# Register your models here.

from hospital.forms import DoctorDetailsForm
#admin reg
from  .models import DoctorDetails 
@admin.register(DoctorDetails)
class DoctorDetailsAdmin(admin.ModelAdmin):
    list_display =('name','email','phone','nid','area','special','daywork')
