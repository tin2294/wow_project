from django.shortcuts import render
from django.http import HttpResponse
from wow.models import Vehicle, Vclass


# Create your views here.
def index(request):
    return HttpResponse("WOW Index")


def bookings(request):
    return render(request, 'bookings.html')


def vehicles(request):
    vehicles_queryset = Vehicle.objects.all().values('make', 'model', 'year', 'classid__class_name', 'classid__daily_rate', 'classid__daily_mileage', 'classid__overage_rate')
    vehicles = list(vehicles_queryset)
    return render(request, 'vehicles.html', {'vehicles': vehicles})


def vehicle_details(request, vehicle_id):
    return render(request, 'vehicle_details.html', {'vehicle_id': vehicle_id})


def booking_details(request, service_id):
    return render(request, 'booking_details.html', {'service_id': service_id})
