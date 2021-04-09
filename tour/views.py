from django.shortcuts import render

# Create your views here.


def about(request):
    context = {
        'title': ' Giới Thiệu - Vietravel',
    }
    return render(request, 'about.html', context)


def contact(request):
    context = {
        'title': 'Liên Hệ - Vietravel',
    }
    return render(request, 'contact.html', context)


def destination(request):
    context = {
        'title': 'Điểm Đến - Vietravel',
    }
    return render(request, 'destinations.html', context)


def index(request):
    context = {
        'title': 'Trang Chủ - Vietravel',
    }
    return render(request, 'index.html', context)
