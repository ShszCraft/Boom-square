# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-25 12:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_blog',
            name='time_add',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='app_blog',
            name='time_now',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
