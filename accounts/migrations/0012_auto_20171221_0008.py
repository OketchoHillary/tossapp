# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-20 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_tuser_share_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuser',
            name='share_code',
            field=models.CharField(blank=True, default=b'9AFB69', max_length=8, unique=True),
        ),
    ]
