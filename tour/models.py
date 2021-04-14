from django.db import models
from django.shortcuts import reverse
# Create your models here.

REGION_CHOICES = [
    ('B', 'Miền Bắc'),
    ('T', 'Miền Trung'),
    ('N', 'Miền Nam')
]


class Destination(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(choices=REGION_CHOICES, max_length=1)
    image = models.ImageField(null=True, blank=True)
    hot = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property  # tránh bị lỗi trang nếu như một ảnh bị xoá
    def imageURL(self):  # giờ đây nó sẽ chỉ hiển thị một khung ảnh trống trên template
        try:  # trên template thay destination.image.url = destination.imageURL
            url = self.image.url
        except:
            url = ''
        return url

    def get_absolute_url(self):
        return reverse("tours", kwargs={'slug': self.name})  # ("app_name: url_name") - có thể ko cần app name


class TourGuide(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, null=True, choices=[('1', 'nam'), ('2', 'nữ')])
    image = models.ImageField(null=True, blank=True)
    birth = models.DateField(null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    english = models.BooleanField(default=False)
    japanese = models.BooleanField(default=False)
    korean = models.BooleanField(default=False)
    chinese = models.BooleanField(default=False)
    french = models.BooleanField(default=False)
    russian = models.BooleanField(default=False)
    spanish = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    departure_place = models.CharField(max_length=200)
    visit_places = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    hot = models.BooleanField(default=False)
    num_seats = models.SmallIntegerField()
    departure_date = models.DateField()
    num_days = models.SmallIntegerField()
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.departure_place, self.destination)


class ImageTour(models.Model):
    image = models.ImageField(null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image.url

    @property               # tránh bị lỗi trang nếu như một ảnh bị xoá
    def imageURL(self):     # giờ đây nó sẽ chỉ hiển thị một khung ảnh trống trên template
        try:                # trên template thay destination.image.url = destination.imageURL
            url = self.image.url
        except:
            url = ''
        return url


class Schedule(models.Model):
    activity = models.TextField(null=True, blank=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.tour)


class Book(models.Model):
    customer_name = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField(max_length=200)
    custumer_addess = models.CharField(max_length=200)
    tour = models.ForeignKey(Tour, on_delete=models.SET_NULL, blank=True, null=True)
    number_people = models.SmallIntegerField()
    total_pay = models.DecimalField(max_digits=15, decimal_places=0)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Banner(models.Model):
    image = models.ImageField(blank=True, null=True)
    show = models.BooleanField(default=True)
