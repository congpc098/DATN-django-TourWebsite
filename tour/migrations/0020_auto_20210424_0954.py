# Generated by Django 3.1.7 on 2021-04-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0019_auto_20210424_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]