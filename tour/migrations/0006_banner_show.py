# Generated by Django 3.1.7 on 2021-04-11 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0005_auto_20210411_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]