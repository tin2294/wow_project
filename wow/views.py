from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("WOW Index")


def bookings(request):
    return render(request, 'bookings.html')

def vehicles(request):
    return render(request, 'vehicles.html')

def vehicle_details(request, vehicle_id):
    return render(request, 'vehicle_details.html', {'vehicle_id': vehicle_id})

def booking_details(request, service_id):
    return render(request, 'booking_details.html', {'service_id': service_id})
