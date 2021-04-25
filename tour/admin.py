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


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('date_booked',)


class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)


admin.site.register(Destination)
admin.site.register(TourGuide)
admin.site.register(Tour, TourAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Feedback, FeedbackAdmin)
