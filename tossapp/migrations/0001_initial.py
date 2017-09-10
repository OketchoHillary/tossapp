# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-26 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('your_name', models.CharField(max_length=30)),
                ('your_email', models.EmailField(max_length=254)),
                ('your_subject', models.CharField(max_length=40)),
                ('your_message', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'Contact Us',
                'verbose_name_plural': 'Contact Us Messages',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=230)),
                ('slug', models.SlugField(max_length=230, unique=True)),
                ('detail', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name_plural': 'Faq',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('display_photo', models.ImageField(default=None, upload_to='games')),
                ('game_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Game_stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bet_amount', models.IntegerField()),
                ('status', models.IntegerField(choices=[(0, 'Lose'), (1, 'Win'), (3, 'Pending')])),
                ('win_amount', models.FloatField(blank=True, default=0.0)),
                ('loss_amount', models.FloatField(blank=True, default=0.0)),
                ('service_fee', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tossapp.Game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(0, 'Success'), (1, 'Information'), (2, 'Warning'), (3, 'Error'), (4, 'Account')], default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_no', models.CharField(max_length=13)),
                ('transaction_type', models.IntegerField(choices=[(0, 'Deposit'), (1, 'Withdraw'), (2, 'Transfer')])),
                ('payment_method', models.IntegerField(choices=[(0, 'Mobile Money'), (1, 'Tossapp transfer')])),
                ('amount', models.FloatField(blank=True, default=0.0)),
                ('status', models.IntegerField(choices=[(0, 'Complete'), (1, 'Pending'), (2, 'Failed')])),
                ('timestamp', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
