# Generated by Django 3.1.7 on 2021-04-13 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0011_auto_20210413_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour'),
        ),
    ]
