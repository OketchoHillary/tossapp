# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20171221_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuser',
            name='share_code',
            field=models.CharField(blank=True, max_length=24, unique=True),
        ),
    ]
