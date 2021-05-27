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
    list_display = ("visit_places", "price", "departure_date", "num_days", "tour_guide")


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('date_booked',)
    list_display = ("tour", "customer_name", "customer_phone", "number_people", "date_booked")


class DestinationAdmin(admin.ModelAdmin):
    list_display = ("name", "region", "hot")


class FeedbackAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ("subject", "cus_name", "message", "date")


class TourGuideAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "email")
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Picture preview'
    thumbnail_preview.allow_tags = True


admin.site.register(Destination, DestinationAdmin)
admin.site.register(TourGuide, TourGuideAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Feedback, FeedbackAdmin)
