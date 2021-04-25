from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('destinations/', views.destination, name="destinations"),
    path('destinations/<slug>/', views.tour_list, name="tours"),
    path('tour-detail/<int:pk>/', views.tour_detail, name="tour-detail"),
    path('booking-successful/', views.book_successful, name="book-successful"),
    path('about/', views.about, name="about"),
    path('search-results/', views.SearchResultsView.as_view(), name="search"),

]
