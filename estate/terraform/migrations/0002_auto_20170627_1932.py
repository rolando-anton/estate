# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-27 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terraform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='disable',
            field=models.BooleanField(default=False, verbose_name='disable'),
        ),
        migrations.AddField(
            model_name='historicalfile',
            name='disable',
            field=models.BooleanField(default=False, verbose_name='disable'),
        ),
    ]