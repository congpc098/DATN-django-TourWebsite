from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect
from django.views.generic import (ListView, DetailView)
# sending email
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string  # render template to body of email
# Create your views here.


def about(request):
    context = {
        'title': ' Giới Thiệu - Vietravel',
        'active2': 'active'
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        feedback = Feedback(cus_name=name, cus_email=email, subject=subject, message=message)
        feedback.save()
        msg = "'Bạn đã gửi phản hồi thành công! Chúng tôi sẽ trả lời bạn trong 24h.'"

        return render(request, 'contact.html', {'msg': msg, 'title': 'Liên Hệ - Vietravel', 'active4': 'active'})

    context = {
        'title': 'Liên Hệ - Vietravel',
        'active4': 'active',
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
    context = {
        'hot_destinations': hot_destinations,
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


def tour_detail(request, pk):
    tour = Tour.objects.get(id=pk)
    context = {
        'title': 'Chi tiết Tour - Vietravel',
        'tour': tour,
    }
    if request.method == "POST":
        name = request.POST['inputName']
        phone = request.POST['inputPhone']
        email = request.POST['inputEmail']
        address = request.POST['inputAddress']
        people = request.POST['inputPeople']
        total = tour.price*int(people)
        book = Book(customer_name=name, customer_phone=phone, customer_email=email, custumer_addess=address, tour=tour, number_people=people, total_pay=total)
        book.save()
        request.session['customer_email'] = email
        request.session['tour_id'] = pk
        return redirect('book-successful')

    return render(request, 'tour_detail.html', context)


def book_successful(request):
    customer_email = request.session.get('customer_email')
    tour_id = request.session.get('tour_id')
    tour = Tour.objects.get(id=tour_id)
    template = render_to_string('template_email.html', {'tour_name': tour.visit_places, 'date': tour.departure_date})

    email = EmailMessage(
        'Vietravel - Đơn đặt tour',
        template,
        settings.EMAIL_HOST_USER,
        [customer_email]
    )
    email.fail_silently = False
    email.send()

    context = {
        'title': 'Cảm ơn bạn - Vietravel',
    }
    return render(request, 'book_successful.html', context)
