# Generated by Django 3.1.7 on 2021-04-14 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0013_auto_20210413_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetour',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='tour.tour'),
        ),
    ]