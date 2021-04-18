from django.contrib import admin
from .models import *  # import tất cả model
# Register your models here.
# https://stackoverflow.com/questions/63325929/django-multiple-pictures-one-product


class ImageTourInline(admin.StackedInline):
    model = ImageTour


class ScheduleInline(admin.StackedInline):
    model = Schedule


class TourAdmin(admin.ModelAdmin):
    inlines = [ImageTourInline, ScheduleInline]


admin.site.register(Destination)
admin.site.register(TourGuide)
admin.site.register(Tour, TourAdmin)
admin.site.register(Book)
