# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 19:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_lotto', '0008_dailylottoticket_tax'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylottoticket',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
