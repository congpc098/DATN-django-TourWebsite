# Generated by Django 3.1.7 on 2021-04-14 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0014_auto_20210414_0914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tour',
            name='hotel',
        ),
        migrations.AlterField(
            model_name='imagetour',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tour.tour'),
        ),
    ]
