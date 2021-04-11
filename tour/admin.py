from django.contrib import admin
from .models import *  # import tất cả model
# Register your models here.

admin.site.register(Destination)
admin.site.register(Schedule)
admin.site.register(TourGuide)
admin.site.register(Image)
admin.site.register(Tour)
admin.site.register(Book)
