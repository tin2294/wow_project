from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bookings/", views.bookings_emp, name="bookings"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("bookings/<str:service_id>", views.rentalservice_details, name="rentalservice_details"),
    path("vehicles/<str:vehicle_id>", views.vehicle_details, name="vehicle_details"),
    path('update_vehicle/<int:vehicle_id>/', views.update_vehicle, name='update_vehicle'),
    path('update_booking/<int:service_id>/', views.update_rentalservice, name='update_rentalservice'),
    path('create_booking/', views.create_rentalservice, name='create_rentalservice'),
]