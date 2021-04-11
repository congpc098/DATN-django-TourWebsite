from django.db import models

# Create your models here.

REGION_CHOICES = [
    ('B', 'Miền Bắc'),
    ('T', 'Miền Trung'),
    ('N', 'Miền Nam')
]


class Destination(models.Model):
    name = models.CharField(max_length=200)
    region = models.CharField(choices=REGION_CHOICES, max_length=1)
    image = models.ImageField(upload_to='static/images')

    def __str__(self):
        return self.name


class Schedule(models.Model):

    visit_places = models.CharField(max_length=200, null=True, blank=True)
    day1 = models.TextField(null=True, blank=True)
    day2 = models.TextField(null=True, blank=True)
    day3 = models.TextField(null=True, blank=True)
    day4 = models.TextField(null=True, blank=True)
    day5 = models.TextField(null=True, blank=True)
    day6 = models.TextField(null=True, blank=True)
    day7 = models.TextField(null=True, blank=True)


class TourGuide(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=1, null=True, choices=[('1', 'nam'), ('2', 'nữ')])
    image = models.ImageField(upload_to='static/images', null=True)
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


class Image(models.Model):
    image1 = models.ImageField(upload_to='static/images', null=True, blank=True)
    image2 = models.ImageField(upload_to='static/images', null=True, blank=True)
    image3 = models.ImageField(upload_to='static/images', null=True, blank=True)
    image4 = models.ImageField(upload_to='static/images', null=True, blank=True)
    image5 = models.ImageField(upload_to='static/images', null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = 'Tour Images'


class Tour(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    departure_place = models.CharField(max_length=200)
    image = models.OneToOneField(Image, on_delete=models.PROTECT, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    hot = models.BooleanField(default=False)
    num_seats = models.SmallIntegerField()
    departure_date = models.DateField()
    num_days = models.SmallIntegerField()
    tour_guide = models.ForeignKey(TourGuide, on_delete=models.SET_NULL, null=True, blank=True)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)
    hotel = models.CharField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.departure_place, self.destination)


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
