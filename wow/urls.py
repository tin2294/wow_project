from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register_account, name="register"),
    path("login/", LoginView.as_view(template_name="wow/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="wow/logout.html"), name="logout"),
    path("profile/", views.view_profile, name="view_profile"),
    path("profile/create", views.create_profile, name="create_profile"),
    path("profile/individual/create", views.create_indiv_cust, name="create_indiv_cust"),
    path("profile/corporate/create", views.create_corp_cust, name="create_corp_cust"),
    path("bookings/", views.bookings_emp, name="bookings"),
    path("vehicles/", views.vehicles, name="vehicles"),
    path("bookings/<str:id>", views.rentalservice_details, name="rentalservice_details"),
    path("vehicles/<str:id>", views.vehicle_details, name="vehicle_details"),
    path("vehicles/<str:id>/book", views.book_vehicle, name="book_vehicle"),
    path("vehicles/<str:id>/bo/book", views.book_vehicle_bo, name="book_vehicle_bo"),
    path('update_vehicle/<int:id>/', views.update_vehicle, name='update_vehicle'),
    path('update_booking/<int:id>/', views.update_rentalservice, name='update_rentalservice'),
    path('create_booking/', views.create_rentalservice, name='create_rentalservice'),
    path('create_vehicle/', views.create_vehicle, name='create_vehicle'),
    # Template not complete
    path('delete_vehicle/<int:id>/', views.delete_vehicle, name='delete_vehicle'),
    # Template not complete
    path('delete_booking/<int:id>/', views.delete_rentalservice, name='delete_rentalservice'),
    # Template exists but is not complete
    path('bookings/<str:id>/checkout', views.checkout, name='checkout')
]