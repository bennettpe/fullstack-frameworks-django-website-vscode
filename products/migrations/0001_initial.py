# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-13 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=254)),
                ('part_name', models.CharField(max_length=100)),
                ('part_number', models.CharField(max_length=30)),
                ('vehicle_model', models.CharField(max_length=25)),
                ('required', models.DecimalField(decimal_places=0, max_digits=3)),
                ('diagram_number', models.DecimalField(decimal_places=0, max_digits=3)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
