from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('destinations/', views.destination, name="destinations"),
    path('destinations/<slug>', views.tour_list, name="tours"),
    path('about/', views.about, name="about"),
    path('booking/', views.booking, name="booking"),

]
