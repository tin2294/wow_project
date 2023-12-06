from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bookings/", views.bookings_emp, name="bookings"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("bookings/<str:service_id>", views.booking_details, name="booking_details"),
    path("vehicles/<str:vehicle_id>", views.vehicle_details, name="vehicle_details"),
]