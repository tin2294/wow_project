import logging
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from wow.models import RentalService, Customer, Vehicle, VClass
from django.contrib.admin.views.decorators import staff_member_required
from .forms import (
    VehicleForm,
    RentalServiceForm,
    RentalServiceUpdateForm,
    VehicleCreationForm,
    AccountRegistrationForm,
    CustomerProfileCreationForm,
    CorpCustCreationForm,
    IndivCustCreationForm,
    RentalServiceCustVehInclForm,
    RentalServiceStaffVehInclForm
)

"""
If we want to designate a view as staff only, we can use the following import
from django.contrib.admin.views.decorators import staff_member_required
Then decorate the view as follows
@staff_member_required
def view_function(request):
    blah blah
"""

# Create your views here.
def index(request):
    return render(request, 'wow/home.html', {})

### Profile and User Related Views ###
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
            return redirect(reverse("create_profile"))
    else:
        reg_form = AccountRegistrationForm()

    return render(request, 'wow/register.html', {"form": reg_form})

@login_required
def view_profile(request):
    user_instance = request.user
    context = {
        "first_name": user_instance.first_name,
        "last_name": user_instance.last_name,
        "email": user_instance.email,
        "is_staff": user_instance.is_staff,
        "account_type": user_instance.customer.cust_type if hasattr(user_instance, 'customer') else "Staff",
    }
    return render(request, 'wow/view_profile.html', context)

@login_required
def create_profile(request):
    if request.method == "POST":
        customer_form = CustomerProfileCreationForm(request.POST)
        if customer_form.is_valid():
            cust_instance = customer_form.save(commit=False)
            cust_instance.user = request.user
            cust_instance.save()
            if cust_instance.cust_type == "I":
                return redirect(reverse("create_indiv_cust"))
            elif cust_instance.cust_type == "C":
                return redirect(reverse("create_corp_cust"))
            else:
                return redirect(reverse("view_profile"))
    else:
        customer_form = CustomerProfileCreationForm()

    return render(request, 'wow/create_profile.html', {"form": customer_form})

@login_required
def create_indiv_cust(request):
    try:
        cust_instance = request.user.customer
    except Customer.DoesNotExist:
        return redirect(reverse("create_profile"))
    else:
        if request.method == "POST":
            indiv_cust_form = IndivCustCreationForm(request.POST)
            if indiv_cust_form.is_valid():
                indiv_cust_instance = indiv_cust_form.save(commit=False)
                indiv_cust_instance.customer = cust_instance
                return redirect(reverse("view_profile"))
        else:
            indiv_cust_form = IndivCustCreationForm()

        return render(request, 'wow/create_indiv_profile.html', {"form": indiv_cust_form})

@login_required
def create_corp_cust(request):
    try:
        cust_instance = request.user.customer
    except Customer.DoesNotExist:
        return redirect(reverse("create_profile"))
    else:
        if request.method == "POST":
            corp_cust_form = CorpCustCreationForm(request.POST)
            if corp_cust_form.is_valid():
                corp_cust_instance = corp_cust_form.save(commit=False)
                corp_cust_instance.customer = cust_instance
                corp_cust_instance.save()
                return redirect(reverse("view_profile"))
        else:
            corp_cust_form = CorpCustCreationForm()

    return render(request, 'wow/create_corp_profile.html', {"form": corp_cust_form})

@login_required
def bookings_emp(request):
    user = request.user
    bookings_query_ind = []
    bookings_query_corp = []
    if user.is_staff:
        bookings_query_ind = RentalService.objects.filter(customer__cust_type='I').select_related(
            'vehicle', 'vehicle__vclass', 'customer', 'customer__indivcust', 'customer__user'
        ).values(
            'id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
            'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle__vclass__class_name', 'vehicle__make', 'vehicle__model',
            'customer__indivcust__license_no', 'customer__indivcust__insurance_co', 'customer__indivcust__insurance_policy_num',
            'customer__user__first_name', 'customer__user__last_name', 'is_active'
        )

        bookings_query_corp = RentalService.objects.filter(customer__cust_type='C').select_related(
            'vehicle', 'vehicle__vclass', 'customer', 'customer__corpcust'
        ).values(
            'id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
            'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle__vclass__class_name', 'vehicle__make', 'vehicle__model',
            'customer__corpcust__company_name', 'customer__corpcust__company_number', 'customer__corpcust__emp_id', 'is_active'
        )
    else:
        if hasattr(user, 'customer'):
            customer = user.customer
            if customer.cust_type == 'I':
                bookings_query_ind = RentalService.objects.filter(customer=customer).select_related(
                    'vehicle', 'vehicle__vclass', 'customer', 'customer__indivcust', 'customer__user'
                ).values(
                    'id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
                    'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle__vclass__class_name', 'vehicle__make',
                    'vehicle__model',
                    'customer__indivcust__license_no', 'customer__indivcust__insurance_co',
                    'customer__indivcust__insurance_policy_num',
                    'customer__user__first_name', 'customer__user__last_name', 'is_active'
                )
                bookings_query_corp = []
            elif customer.cust_type == 'C':
                bookings_query_corp = RentalService.objects.filter(customer=customer).select_related(
                    'vehicle', 'vehicle__vclass', 'customer', 'customer__corpcust'
                ).values(
                    'id', 'pickup_street', 'pickup_state', 'pickup_country', 'pickup_zipcode', 'pickup_date',
                    'dropoff_date', 'start_odometer', 'end_odometer', 'vehicle__vclass__class_name', 'vehicle__make',
                    'vehicle__model',
                    'customer__corpcust__company_name', 'customer__corpcust__company_number',
                    'customer__corpcust__emp_id', 'is_active'
                )
                bookings_query_ind = []

    bookings = list(bookings_query_ind) + list(bookings_query_corp)
    return render(request, 'wow/bookings_emp.html', {'bookings': bookings})


def vehicles(request):
    vehicles_queryset = Vehicle.objects.all().values('id', 'make', 'model', 'year', 'vclass__class_name', 'vclass__daily_rate', 'vclass__daily_mileage', 'vclass__overage_rate')
    vehicles = list(vehicles_queryset)
    return render(request, 'wow/vehicles.html', {'vehicles': vehicles})


def vehicle_details(request, id):
    vehicle = Vehicle.objects.get(id=id)
    return render(request, 'wow/vehicle_details.html', {'vehicle': vehicle})

@login_required
def book_vehicle(request, id):
    user = request.user
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        form = RentalServiceCustVehInclForm(request.POST)
        if form.is_valid():
            if user.customer:
                new_service = form.save(commit=False)
                new_service.customer = user.customer
                new_service.vehicle = vehicle
                new_service.save()
                return redirect('checkout')
    else:
        form = RentalServiceCustVehInclForm()
    return render(request, 'wow/rentalservice_creation.html', {'form': form})


def book_vehicle_bo(request, id):
    vehicle = Vehicle.objects.get(id=id)
    if request.method == 'POST':
        form = RentalServiceStaffVehInclForm(request.POST)
        if form.is_valid():
            new_service = form.save(commit=False)
            new_service.vehicle = vehicle
            new_service.save()
            return redirect('checkout')
    else:
        form = RentalServiceStaffVehInclForm()
    return render(request, 'wow/rentalservice_creation.html', {'form': form})


def rentalservice_details(request, id):
    rentalservice = RentalService.objects.get(id=id)
    return render(request, 'wow/rentalservice_details.html', {'rentalservice': rentalservice})

@staff_member_required
def update_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vehicle_details', args=[id]))
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'wow/vehicle_details.html', {'form': form, 'vehicle': vehicle})

@login_required
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

@login_required
def create_rentalservice(request):
    user = request.user
    if request.method == 'POST':
        form = RentalServiceForm(request.POST)
        if form.is_valid():
            if user.is_staff:
                form.save()
                return redirect('checkout')
    else:
        form = RentalServiceForm()
    return render(request, 'wow/rentalservice_creation.html', {'form': form})

@staff_member_required
def create_vehicle(request):
    if request.method == 'POST':
        form = VehicleCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vehicles'))
    else:
        form = VehicleCreationForm()
    return render(request, 'wow/vehicle_creation.html', {'form': form})

@staff_member_required
def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, pk=id)
    if request.method == 'POST':
        vehicle.delete()
        return HttpResponseRedirect(reverse('vehicles'))
    return render(request, 'wow/vehicle_delete.html', {'vehicle': vehicle})

@login_required
def delete_rentalservice(request, id):
    rentalservice = get_object_or_404(RentalService, pk=id)
    if request.method == 'POST':
        rentalservice.delete()
        return HttpResponseRedirect(reverse('bookings'))
    return render(request, 'wow/rentalservice_delete.html', {'rentalservice': rentalservice})

# Checkout with an existing payment method
@login_required
def checkout(request):
    pass


def return_vehicle(request, id):
    service = RentalService.objects.get(id=id)
    service.is_active = False
    service.save()
    return HttpResponseRedirect(reverse('bookings'))