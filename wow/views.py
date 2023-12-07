import logging
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from wow.models import RentalService, Customer, Vehicle, Vclass
from django.contrib.auth.decorators import login_required
from .forms import (
    AccountRegistrationForm,
    CustomerProfileCreationForm,
    EmployeeProfileCreationForm,
    VehicleForm,
    RentalServiceForm,
    RentalServiceUpdateForm,
    VehicleCreationForm
)


# Create your views here.
def register_account(request):
    if request.method == "POST":
        reg_form = AccountRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            reg_form_data = reg_form.cleaned_data
            user_auth = authenticate(
                username=reg_form_data["username"], password=reg_form_data["password1"]
            )
            login(request, user_auth)
            if reg_form_data["is_staff"]:
                return redirect(reverse("create_employee_profile"))
            else:
                return redirect(reverse("create_customer_profile"))
    else:
        reg_form = AccountRegistrationForm()

    return render(request, 'wow/register.html', {"form": reg_form})


@login_required
def create_customer_profile(request):
    logger = logging.getLogger()
    if not request.user.is_staff:
        if request.method == "POST":
            customer_form = CustomerProfileCreationForm(request.POST)
            if customer_form.is_valid():
                cust_instance = customer_form.save(commit=False)
                cust_instance.user = request.user
                cust_instance.save()
                logger.info(cust_instance)
                return redirect(reverse("view_profile"))
        else:
            customer_form = CustomerProfileCreationForm()
            return render(request, 'wow/create_profile.html', {"form": customer_form})
    else:
        # Change this to a 403 later
        return HttpResponse("You can't view this")


@login_required
def create_employee_profile(request):
    logger = logging.getLogger()
    if request.user.is_staff:
        if request.method == "POST":
            employee_form = EmployeeProfileCreationForm(request.POST)
            if employee_form.is_valid():
                emp_instance = employee_form.save(commit=False)
                emp_instance.user = request.user
                emp_instance.save()
                logger.info(emp_instance)
                return redirect(reverse("view_profile"))
        else:
            employee_form = EmployeeProfileCreationForm()
            return render(request, 'wow/create_profile.html', {"form": employee_form})
    else:
        # Change this to a 403 later
        return HttpResponse("You can't view this")


def view_profile(request):
    user_instance = request.user
    context = {
        "first_name": user_instance.first_name,
        "last_name": user_instance.last_name,
        "email": user_instance.email,
        "is_staff": user_instance.is_staff
    }
    return render(request, 'wow/view_profile.html', context)


def index(request):
    return HttpResponse("WOW Index")


def bookings_emp(request):
    bookings_query_ind = RentalService.objects.filter(
        cust_id__cust_type='I'
    ).values(
        'service_id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
        'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle_id__classid__class_name', 'vehicle_id__make', 'vehicle_id__model',
        'cust_id__indivcust__fname', 'cust_id__indivcust__lname', 'cust_id__indivcust__licenseno',
        'cust_id__indivcust__insurance_co', 'cust_id__indivcust__insurancep_no'
    )
    bookings_query_corp = RentalService.objects.filter(
        cust_id__cust_type='C'
    ).values(
        'service_id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
        'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle_id__classid__class_name', 'vehicle_id__make', 'vehicle_id__model',
        'cust_id__corpcust__company_name', 'cust_id__corpcust__company_no', 'cust_id__corpcust__emp_id'
    )
    bookings = list(bookings_query_ind) + list(bookings_query_corp)
    return render(request, 'wow/bookings_emp.html', {'bookings': bookings})



def vehicles(request):
    vehicles_queryset = Vehicle.objects.all().values('vehicle_id', 'make', 'model', 'year', 'classid__class_name', 'classid__daily_rate', 'classid__daily_mileage', 'classid__overage_rate')
    vehicles = list(vehicles_queryset)
    return render(request, 'wow/vehicles.html', {'vehicles': vehicles})


def vehicle_details(request, vehicle_id):
    vehicle = Vehicle.objects.get(vehicle_id=vehicle_id)
    form = RentalServiceForm()
    return render(request, 'wow/vehicle_details.html', {'vehicle': vehicle, 'form': form})


def rentalservice_details(request, service_id):
    rentalservice = RentalService.objects.get(service_id=service_id)
    return render(request, 'wow/rentalservice_details.html', {'rentalservice': rentalservice})


def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vehicle_details', args=[vehicle_id]))  # Replace with your URL
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'wow/vehicle_details.html', {'form': form, 'vehicle': vehicle})


def update_rentalservice(request, service_id):
    rentalservice = get_object_or_404(RentalService, pk=service_id)
    if request.method == 'POST':
        form = RentalServiceUpdateForm(request.POST, instance=rentalservice)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('rentalservice_details', args=[service_id]))
    else:
        form = RentalServiceUpdateForm(instance=rentalservice)
    return render(request, 'wow/rentalservice_details.html', {'form': form, 'service': rentalservice})


def create_rentalservice(request):
    if request.method == 'POST':
        form = RentalServiceForm(request.POST)
        if form.is_valid():
            # Get the next available service_id from the database
            next_service_id = RentalService.objects.all().order_by('-service_id').first().service_id + 1
            new_service = form.save(commit=False)
            new_service.service_id = next_service_id
            new_service.save()
            return HttpResponseRedirect(reverse('bookings'))
    else:
        form = RentalServiceForm()
    return render(request, 'wow/rentalservice_creation.html', {'form': form})


def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vehicles'))
    else:
        form = VehicleCreationForm()
    return render(request, 'wow/vehicle_creation.html', {'form': form})


def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    if request.method == 'POST':
        vehicle.delete()
        return HttpResponseRedirect(reverse('vehicles'))
    return render(request, 'wow/vehicle_delete.html', {'vehicle': vehicle})


def delete_rentalservice(request, service_id):
    rentalservice = get_object_or_404(RentalService, pk=service_id)
    if request.method == 'POST':
        rentalservice.delete()
        return HttpResponseRedirect(reverse('bookings'))
    return render(request, 'wow/rentalservice_delete.html', {'rentalservice': rentalservice})


def checkout(request):
    return render(request, 'wow/checkout.html')
