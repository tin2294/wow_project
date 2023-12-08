from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from wow.models import RentalService, Customer, Vehicle, VClass
from .forms import VehicleForm, RentalServiceForm, RentalServiceUpdateForm, VehicleCreationForm


# Create your views here.
def index(request):
    return HttpResponse("WOW Index")


def bookings_emp(request):
    bookings_query_ind = RentalService.objects.filter(customer__cust_type='I').select_related(
        'vehicle', 'vehicle__class_id', 'customer', 'customer__indivcust', 'customer__user'
    ).values(
        'id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
        'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle__class_id__class_name', 'vehicle__make', 'vehicle__model',
        'customer__indivcust__license_no', 'customer__indivcust__insurance_co', 'customer__indivcust__insurance_policy_num',
        'customer__user__first_name', 'customer__user__last_name'
    )

    bookings_query_corp = RentalService.objects.filter(customer__cust_type='C').select_related(
        'vehicle', 'vehicle__class_id', 'customer', 'customer__corpcust'
    ).values(
        'id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
        'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle__class_id__class_name', 'vehicle__make', 'vehicle__model',
        'customer__corpcust__company_name', 'customer__corpcust__company_number', 'customer__corpcust__emp_id'
    )

    bookings = list(bookings_query_ind) + list(bookings_query_corp)
    return render(request, 'wow/bookings_emp.html', {'bookings': bookings})


def vehicles(request):
    vehicles_queryset = Vehicle.objects.all().values('id', 'make', 'model', 'year', 'class_id__class_name', 'class_id__daily_rate', 'class_id__daily_mileage', 'class_id__overage_rate')
    vehicles = list(vehicles_queryset)
    return render(request, 'wow/vehicles.html', {'vehicles': vehicles})


def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(id=id)
    form = RentalServiceForm()
    return render(request, 'wow/vehicle_details.html', {'vehicle': vehicle, 'form': form})


def rentalservice_details(request, id):
    rentalservice = RentalService.objects.get(id=id)
    return render(request, 'wow/rentalservice_details.html', {'rentalservice': rentalservice})


def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vehicle_details', args=[id]))
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'wow/vehicle_details.html', {'form': form, 'vehicle': vehicle})


def update_rentalservice(request, id):
    rentalservice = get_object_or_404(RentalService, pk=id)
    if request.method == 'POST':
        form = RentalServiceUpdateForm(request.POST, instance=rentalservice)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rentalservice_details', args=[id]))
    else:
        form = RentalServiceUpdateForm(instance=rentalservice)
    return render(request, 'wow/rentalservice_details.html', {'form': form, 'service': rentalservice})


def create_rentalservice(request):
    if request.method == 'POST':
        form = RentalServiceForm(request.POST)
        if form.is_valid():
            # Get the next available service_id from the database
            next_service_id = RentalService.objects.all().order_by('-id').first().id + 1
            new_service = form.save(commit=False)
            new_service.id = next_service_id
            new_service.save()
            return HttpResponseRedirect(reverse('bookings'))
    else:
        form = RentalServiceForm()
    return render(request, 'wow/rentalservice_creation.html', {'form': form})


def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleCreationForm(request.POST)
        if form.is_valid():
            next_vehicle_id = Vehicle.objects.all().order_by('-id').first().id + 1
            new_vehicle = form.save(commit=False)
            new_vehicle.id = next_vehicle_id
            new_vehicle.save()
            return HttpResponseRedirect(reverse('vehicles'))
    else:
        form = VehicleCreationForm()
    return render(request, 'wow/vehicle_creation.html', {'form': form})


def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id)
    if request.method == 'POST':
        vehicle.delete()
        return HttpResponseRedirect(reverse('vehicles'))
    return render(request, 'wow/vehicle_delete.html', {'vehicle': vehicle})


def delete_rentalservice(request, id):
    rentalservice = get_object_or_404(RentalService, pk=id)
    if request.method == 'POST':
        rentalservice.delete()
        return HttpResponseRedirect(reverse('bookings'))
    return render(request, 'wow/rentalservice_delete.html', {'rentalservice': rentalservice})


def checkout(request):
    return render(request, 'wow/checkout.html')
