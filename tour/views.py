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
    destinations = Destination.objects.filter(hot=False)[:5]
    # banners = Banner.objects.values_list('image', flat=True)  # lấy ra list các giá trị của cột image có show=True. If you only pass in a single field, you can also pass in the 'flat' parameter. If True, this will mean the returned results are single values, rather than one-tuples
    context = {
        'hot_destinations': hot_destinations,
        'destinations': destinations,
        'title': 'Trang Chủ - Vietravel',
        'active1': 'active',
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


# class DestinationListView(ListView):
    model = Destination                   # by default, Class-based Views look for template 'tour/destination_list.html' - <app>/<modelname>_list.html. And the need to change context variable name to 'object_list'
    template_name = 'index.html'          # so web need to reference to our different template

    def get_context_data(self, **kwargs):  # ghi đè context khi muốn thêm hoặc thay đổi context
        hot_destinations = Destination.objects.filter(hot=True)[:10]
        context = super().get_context_data(**kwargs)
        context = {
            'hot_destinations': hot_destinations,
            'title': 'Trang Chủ - Vietravel',
            'active1': 'active',
        }
        return context


def booking(request):
    context = {
        'title': 'Đặt Tour - Vietravel',
    }
    return render(request, 'booking.html', context)
