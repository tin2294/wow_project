from django.shortcuts import render
from django.http import HttpResponse
from wow.models import RentalService, Customer

# Comment to commit
# Create your views here.
def index(request):
    return HttpResponse("WOW Index")


def bookings_emp(request):
    bookings_query = RentalService.objects.all().values('pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date', 'dropoff_date', 'start_odometer', 'end_odometer', 'cust_id__cust_type', 'vehicle_id__make', 'vehicle_id__model')
    bookings = list(bookings_query)
    return render(request, 'bookings_emp.html', {'bookings': bookings})

def vehicles(request):
    return render(request, 'vehicles.html')

def vehicle_details(request, vehicle_id):
    return render(request, 'vehicle_details.html', {'vehicle_id': vehicle_id})

def booking_details(request, service_id):
    return render(request, 'booking_details.html', {'service_id': service_id})
