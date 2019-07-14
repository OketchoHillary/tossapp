# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-22 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_lotto', '0002_auto_20190622_1506'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailylotto',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterField(
            model_name='dailylotto',
            name='lotto_type',
            field=models.CharField(choices=[('D', 'Daily'), ('H', 'Hourly'), ('Q', 'Quarterly')], max_length=1),
        ),
        migrations.AlterField(
            model_name='dailylotto',
            name='start_date',
            field=models.DateTimeField(default='2019-06-22T15:22:13'),
        ),
    ]