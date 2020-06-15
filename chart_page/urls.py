"""seoul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path, include

from chart_page import views

app_name = 'chart'

urlpatterns = [
    url(r'^traffic/?$', views.traffic, name='traffic'),
    url(r'^education/?$', views.education, name='education'),
    url(r'^environment/?$', views.environment, name='environment'),
    url(r'^medical_crime/?$', views.medical_crime, name='medical_crime'),
    url(r'^result/?$', views.result, name='result'),
    url(r'^rank/?$', views.rank, name='rank'),
    path('traffic-chart/', views.traffic_chart, name='traffic-chart'),
    path('parking-chart/', views.parking_chart, name='parking-chart'),
    path('commute-chart/', views.commute_chart, name='commute-chart'),
    path('school_num-chart/', views.school_num_chart, name='school_num-chart'),
    path('student_num-chart/', views.student_num_chart, name='student_num-chart'),
    path('teacher_num-chart/', views.teacher_num_chart, name='teacher_num-chart'),
    path('park-chart/', views.park_chart, name='park-chart'),
    path('garbage-chart/', views.garbage_chart, name='garbage-chart'),
    path('dust-chart/', views.dust_chart, name='dust-chart'),
    path('green-chart/', views.green_chart, name='green-chart'),
    path('hospital_sickbed-chart/', views.hospital_sickbed_chart, name='hospital_sickbed-chart'),
    path('crime-chart/', views.crime_chart, name='crime-chart'),
    path('pharmacy-chart/', views.pharmacy_chart, name='pharmacy-chart'),
    path('seoul_traffic-chart/', views.seoul_traffic_chart, name='seoul_traffic-chart'),
    path('seoul_medical-chart/', views.seoul_medical_chart, name='seoul_medical-chart'),
    path('seoul_envi-chart/', views.seoul_envi_chart, name='seoul_envi-chart'),
    path('seoul_education-chart/', views.seoul_edu_chart, name='seoul_education-chart'),
]
