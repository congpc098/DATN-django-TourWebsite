from django.shortcuts import render
from .models import *
from django.views.generic import (ListView, DetailView)
# Create your views here.


def about(request):
    context = {
        'title': ' Giới Thiệu - Vietravel',
        'active2': 'active'
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'Liên Hệ - Vietravel',
        'active4': 'active'
    }
    return render(request, 'contact.html', context)


def destination(request):
    destinations = Destination.objects.all()
    context = {
        'destinations': destinations,
        'title': 'Điểm Đến - Vietravel',
        'active3': 'active'
    }
    return render(request, 'destinations.html', context)


def index(request):
    hot_destinations = Destination.objects.filter(hot=True)[:10]  # lấy 10 cái đầu tiên
    # banners = Banner.objects.values_list('image', flat=True)  # lấy ra list các giá trị của cột image có show=True. If you only pass in a single field, you can also pass in the 'flat' parameter. If True, this will mean the returned results are single values, rather than one-tuples
    banners = Banner.objects.filter(show=True)
    context = {
        'hot_destinations': hot_destinations,
        'title': 'Trang Chủ - Vietravel',
        'active1': 'active',
        'banners': banners,
    }
    return render(request, 'index.html', context)


def tour_list(request, slug):
    tours = Tour.objects.filter(destination__name=slug)  # https://stackoverflow.com/questions/27421794/retrieve-foreign-key-object-field-django
    context = {
        'title': 'Tours - Vietravel',
        'tours': tours,
        'destination': slug,
    }
    return render(request, 'tours.html', context)


def tour_detail(request, pk):
    tour = Tour.objects.get(id=pk)
    context = {
        'title': 'Chi tiết Tour - Vietravel',
        'tour': tour,

    }
    return render(request, 'tour_detail.html', context)


def booking(request):
    context = {
        'title': 'Đặt Tour - Vietravel',
    }
    return render(request, 'booking.html', context)
