# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-07 11:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_lotto', '0004_auto_20170907_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylotto',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='dailylottoresult',
            name='draw_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
