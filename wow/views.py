from django.shortcuts import render
from django.http import HttpResponse
from wow.models import RentalService, Customer, Vehicle, Vclass


# Create your views here.
def index(request):
    return HttpResponse("WOW Index")


def bookings_emp(request):
    bookings_query_ind = RentalService.objects.filter(
        cust_id__cust_type='I'
    ).values(
        'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
        'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle_id__classid__class_name', 'vehicle_id__make', 'vehicle_id__model',
        'cust_id__indivcust__fname', 'cust_id__indivcust__lname', 'cust_id__indivcust__licenseno',
        'cust_id__indivcust__insurance_co', 'cust_id__indivcust__insurancep_no'
    )
    bookings_query_corp = RentalService.objects.filter(
        cust_id__cust_type='C'
    ).values(
        'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
        'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle_id__classid__class_name', 'vehicle_id__make', 'vehicle_id__model',
        'cust_id__corpcust__company_name', 'cust_id__corpcust__company_no', 'cust_id__corpcust__emp_id'
    )
    bookings = list(bookings_query_ind) + list(bookings_query_corp)
    return render(request, 'bookings_emp.html', {'bookings': bookings})

def vehicles(request):
    vehicles_queryset = Vehicle.objects.all().values('make', 'model', 'year', 'classid__class_name', 'classid__daily_rate', 'classid__daily_mileage', 'classid__overage_rate')
    vehicles = list(vehicles_queryset)
    return render(request, 'vehicles.html', {'vehicles': vehicles})


def vehicle_details(request, vehicle_id):
    return render(request, 'vehicle_details.html', {'vehicle_id': vehicle_id})

def booking_details(request, service_id):
    return render(request, 'booking_details.html', {'service_id': service_id})
