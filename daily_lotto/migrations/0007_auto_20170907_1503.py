# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-07 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_lotto', '0006_auto_20170907_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylottoticket',
            name='purchased_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
