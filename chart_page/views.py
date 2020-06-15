from django.db.models import Sum
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse

from chart_page.models import *


def traffic(request):
    return render(request, 'chart_page/traffic.html')

def education(request):
    return render(request, 'chart_page/education.html')

def result(request):
    return render(request, 'chart_page/result.html')

def rank(request):
    return render(request, 'chart_page/rank.html')

def environment(request):
    return render(request, 'chart_page/environment.html')

def medical_crime(request):
    return render(request, 'chart_page/medical_crime.html')

def traffic_chart(request):
    labels = []
    data = []

    queryset = Traffic.objects.values('gu__gu').annotate(car=Sum('register_car')).order_by('-car')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['car'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def parking_chart(request):
    labels = []
    data = []

    queryset = Traffic.objects.values('gu__gu').annotate(parking=Sum('parking_lot')).order_by('-parking')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['parking'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def commute_chart(request):
    labels = []
    bus = []
    trail = []
    bus_trail = []
    mycar = []

    queryset = Traffic.objects.values('gu__gu','bus','trail','bus_trail','mycar')
    for entry in queryset:
        labels.append(entry['gu__gu'])
        bus.append(entry['bus'])
        trail.append(entry['trail'])
        bus_trail.append(entry['bus_trail'])
        mycar.append(entry['mycar'])

    return JsonResponse(data={
        'labels': labels,
        'bus': bus,
        'trail': trail,
        'bus_trail': bus_trail,
        'mycar': mycar,
    })

def school_num_chart(request):
    labels = []
    garden = []
    element = []
    middle = []
    high = []

    queryset = Education.objects.values('gu__gu', 'garden', 'element', 'middle', 'high')
    for entry in queryset:
        labels.append(entry['gu__gu'])
        garden.append(entry['garden'])
        element.append(entry['element'])
        middle.append(entry['middle'])
        high.append(entry['high'])

    return JsonResponse(data={
        'labels': labels,
        'garden': garden,
        'element': element,
        'middle': middle,
        'high': high,
    })

def student_num_chart(request):
    labels = []
    garden_num = []
    element_num = []
    middle_num = []
    high_num = []

    queryset = Education.objects.values('gu__gu', 'garden_num', 'element_num', 'middle_num', 'high_num')
    for entry in queryset:
        labels.append(entry['gu__gu'])
        garden_num.append(entry['garden_num'])
        element_num.append(entry['element_num'])
        middle_num.append(entry['middle_num'])
        high_num.append(entry['high_num'])

    return JsonResponse(data={
        'labels': labels,
        'garden_num': garden_num,
        'element_num': element_num,
        'middle_num': middle_num,
        'high_num': high_num,
    })

def teacher_num_chart(request):
    labels = []
    garden_gyo = []
    element_gyo = []
    middle_gyo = []
    high_gyo = []

    queryset = Education.objects.values('gu__gu', 'garden_gyo', 'element_gyo', 'middle_gyo', 'high_gyo')
    for entry in queryset:
        labels.append(entry['gu__gu'])
        garden_gyo.append(entry['garden_gyo'])
        element_gyo.append(entry['element_gyo'])
        middle_gyo.append(entry['middle_gyo'])
        high_gyo.append(entry['high_gyo'])

    return JsonResponse(data={
        'labels': labels,
        'garden_gyo': garden_gyo,
        'element_gyo': element_gyo,
        'middle_gyo': middle_gyo,
        'high_gyo': high_gyo,
    })

def seoul_traffic_chart(request):
    labels = []
    data = []

    queryset = SeoulData.objects.values('gu__gu').annotate(traffic=Sum('traffic')).order_by('-traffic')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['traffic'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def seoul_medical_chart(request):
    labels = []
    medical = []
    medical_room = []

    queryset = SeoulData.objects.values('gu__gu','medical','medical_room').order_by('-medical_room')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        medical.append(entry['medical'])
        medical_room.append(entry['medical_room'])
    return JsonResponse(data={
        'labels': labels,
        'medical': medical,
        'medical_room' : medical_room
    })

def seoul_envi_chart(request):
    labels = []
    data = []

    queryset = SeoulData.objects.values('gu__gu','environment').order_by('-environment')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['environment'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def seoul_edu_chart(request):
    labels = []
    data = []

    queryset = SeoulData.objects.values('gu__gu', 'education').order_by('-education')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['education'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def park_chart(request):
    labels = []
    data = []

    queryset = EnvironmentData.objects.values('gu__gu', 'park').order_by('-park')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['park'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def garbage_chart(request):
    labels = []
    data = []

    queryset = EnvironmentData.objects.values('gu__gu', 'garbage').order_by('-garbage')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['garbage'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def dust_chart(request):
    labels = []
    data = []

    queryset = EnvironmentData.objects.values('gu__gu', 'dust').order_by('-dust')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['dust'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def green_chart(request):
    labels = []
    data = []

    queryset = EnvironmentData.objects.values('gu__gu', 'green').order_by('-green')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['green'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def hospital_sickbed_chart(request):
    labels = []
    hospital = []
    sickbed = []

    queryset = Medical_CrimeData2.objects.values('gu__gu', 'hospital', 'sickbed').order_by('-sickbed')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        hospital.append(entry['hospital'])
        sickbed.append(entry['sickbed'])
    return JsonResponse(data={
        'labels': labels,
        'hospital': hospital,
        'sickbed': sickbed,
    })

def crime_chart(request):
    labels = []
    crime_occ = []
    crime_arr = []

    queryset = Medical_CrimeData2.objects.values('gu__gu', 'crime_occ', 'crime_arr').order_by('-crime_occ')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        crime_occ.append(entry['crime_occ'])
        crime_arr.append(entry['crime_arr'])
    return JsonResponse(data={
        'labels': labels,
        'crime_occ': crime_occ,
        'crime_arr': crime_arr,
    })

def pharmacy_chart(request):
    labels = []
    data = []

    queryset = Medical_CrimeData2.objects.values('gu__gu', 'pharmacy').order_by('-pharmacy')

    for entry in queryset:
        labels.append(entry['gu__gu'])
        data.append(entry['pharmacy'])
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })