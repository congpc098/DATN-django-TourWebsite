# Generated by Django 3.1.7 on 2021-04-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_auto_20210411_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='hot',
            field=models.BooleanField(default=True),
        ),
    ]