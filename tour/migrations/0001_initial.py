# Generated by Django 3.1.7 on 2021-04-10 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('region', models.CharField(choices=[('B', 'Miền Bắc'), ('T', 'Miền Trung'), ('N', 'Miền Nam')], max_length=1)),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='static/images')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='static/images')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day1', models.TextField(blank=True, null=True)),
                ('day2', models.TextField(blank=True, null=True)),
                ('day3', models.TextField(blank=True, null=True)),
                ('day4', models.TextField(blank=True, null=True)),
                ('day5', models.TextField(blank=True, null=True)),
                ('day6', models.TextField(blank=True, null=True)),
                ('day7', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TourGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[(1, 'nam'), (2, 'nữ')], max_length=1, null=True)),
                ('image', models.ImageField(null=True, upload_to='static/images')),
                ('birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=200)),
                ('english', models.BooleanField(default=False)),
                ('japanese', models.BooleanField(default=False)),
                ('korean', models.BooleanField(default=False)),
                ('chinese', models.BooleanField(default=False)),
                ('france', models.BooleanField(default=False)),
                ('russian', models.BooleanField(default=False)),
                ('spanish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_place', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=0, max_digits=8)),
                ('num_seats', models.SmallIntegerField()),
                ('departure_date', models.DateField()),
                ('num_days', models.SmallIntegerField()),
                ('hotel', models.CharField(max_length=200)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.destination')),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tour.image')),
                ('schedule', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tour.schedule')),
                ('tour_guide', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.tourguide')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_phone', models.CharField(max_length=15)),
                ('customer_email', models.EmailField(max_length=200)),
                ('custumer_addess', models.CharField(max_length=200)),
                ('number_people', models.SmallIntegerField()),
                ('total_pay', models.DecimalField(decimal_places=0, max_digits=15)),
                ('date_booked', models.DateTimeField(auto_now_add=True)),
                ('tour', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tour.tour')),
            ],
        ),
    ]