from django.db import models
#image ar time ,date debr jonno bellow
import datetime
import os

    
# Create your models here.
AREA=(               
    ('Dhaka', 'Dhaka'),
    ('Chattogram', 'Chattogram'),
    (' Khulna', ' Khulna'),
    ('Barishal', 'Barishal'),
    ('Rajshahi', 'Rajshahi'),
    ('Sylhet', 'Sylhet'),
    ('Rangpur', 'Rangpur'),
    ('Mymensingh', 'Mymensingh'),
)
SPECIALITY=(                
    ('Nerulogy medicine', 'Nerulogy medicine'),
    ('Diabetology', 'Diabetology'),
    ('Chest medicine', 'Chest medicine'),
    ('Gastroenterologist medicine', 'Gastroenterologist medicine'),
    ('Nerulogy Surgery', 'Nerulogy Surgery'),
    ('Cancer Specialist', 'Cancer Specialist'),
   
)
DAY=(
    ('Saturday','Saturday'),
    ('Sunday','Sunday'),
    ('Monday','Monday'),
    ('Tuesday','Tuesday'),
    ('Wednesday','Wednesday'),
    ('Thursday','Thursday'),
    ('Friday','Friday'),
    
)
class DoctorDetails(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField() #views or page need if condition for 11 digit
    nid=models.IntegerField()
    area=models.CharField(choices=AREA, max_length=200)
    special=models.CharField(choices=SPECIALITY, max_length=200)
    daywork=models.CharField(choices=DAY, max_length=200)
    
    class Meta:
        verbose_name = "DoctorDetails"
        verbose_name_plural = "DoctorDetails"


BOOL=(
    ('Yes','Yes'),
    ('No','No'),
)
class Patient(models.Model):
    doctor_name=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()
    location=models.CharField(max_length=200)
    patient_category=models.CharField(choices=BOOL, max_length=50)
    details=models.CharField(max_length=300)
    

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patient"



