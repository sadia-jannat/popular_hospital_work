"""hospitalsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#image add ar jonno
from django.conf import settings
from django.conf.urls.static import static

from hospital import views

#API
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.doctorformfill, name='doctorformfill'),
    path('details/', views.details, name="details"),
    path('testsearch/', views.testsearch, name="testsearch"),
    path('appointment/<str:pk>', views.appointment, name="appointment"),
    path('dashboard_appointment/', views.dashboard_appointment, name='dashboard_appointment'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard_appointment_delete/<int:id>/', views.dashboard_appointment_delete, name='dashboard_appointment_delete'),
    path('dashboard_appointment_serial/<int:id>/', views.dashboard_appointment_serial, name='dashboard_appointment_serial'),
    path('appointmentform/<str:pk>', views.appointmentform, name="appointmentform"),
    path('sendemail/', views.sendemail, name="sendemail"),
    path('home/', views.home, name="home"),
    
]
