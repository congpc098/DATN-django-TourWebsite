from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="tour"),
    path('contact/', views.contact, name="contact"),
    path('destinations/', views.destination, name="destinations"),
    path('about/', views.about, name="about"),
    path('booking/', views.booking, name="booking"),

]
