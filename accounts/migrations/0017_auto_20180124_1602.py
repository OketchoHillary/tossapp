# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-24 13:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20180124_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuser',
            name='share_code',
            field=models.CharField(blank=True, max_length=14, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Username must not exceed 10 characters', regex='^.{10}$')]),
        ),
    ]
