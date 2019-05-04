# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-04-09 06:36
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
            name='CommissionSum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dates', models.DateTimeField(auto_now_add=True)),
                ('commission_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DailyLotto',
            fields=[
                ('lotto_id', models.AutoField(primary_key=True, serialize=False)),
                ('lotto_type', models.CharField(choices=[(b'D', b'Daily'), (b'H', b'Hourly'), (b'S', b'Quarterly')], max_length=1)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(editable=False)),
                ('win1', models.IntegerField(default=0)),
                ('win2', models.IntegerField(default=0)),
                ('win3', models.IntegerField(default=0)),
                ('win4', models.IntegerField(default=0)),
                ('win5', models.IntegerField(default=0)),
                ('win6', models.IntegerField(default=0)),
                ('jack_pot', models.IntegerField(default=0)),
                ('backup_jackpot', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['-start_date'],
                'db_table': 'lotto',
            },
        ),
        migrations.CreateModel(
            name='DailyLottoResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draw_date', models.DateTimeField(auto_now_add=True)),
                ('winners', models.CharField(max_length=177)),
                ('hits_number_prize', models.IntegerField()),
                ('service_commission', models.IntegerField(default=25)),
                ('prize', models.IntegerField()),
                ('daily_lotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_lotto.DailyLotto')),
            ],
            options={
                'db_table': 'lotto_results',
            },
        ),
        migrations.CreateModel(
            name='DailyLottoTicket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField(default=500)),
                ('purchased_time', models.DateTimeField(auto_now_add=True)),
                ('n1', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name=b'Number 1')),
                ('n2', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name=b'Number 2')),
                ('n3', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name=b'Number 3')),
                ('n4', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name=b'Number 4')),
                ('n5', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name=b'Number 5')),
                ('n6', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30)], verbose_name=b'Number 6')),
                ('ticket_prize', models.IntegerField(default=0)),
                ('hits', models.IntegerField(default=0)),
                ('tax', models.IntegerField(default=0)),
                ('daily_lotto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_lotto.DailyLotto')),
                ('player_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-purchased_time'],
                'db_table': 'lotto_tickets',
                'verbose_name_plural': 'Daily Lotto Tickets',
            },
        ),
        migrations.CreateModel(
            name='DailyQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_commission', models.IntegerField(default=0)),
                ('six_number_prize_pool', models.IntegerField(default=0)),
                ('five_number_prize_pool', models.IntegerField(default=0)),
                ('four_number_prize_pool', models.IntegerField(default=0)),
                ('three_number_prize_pool', models.IntegerField(default=0)),
                ('six_number_prize_pool_commission', models.IntegerField(default=0)),
                ('five_number_prize_pool_commission', models.IntegerField(default=0)),
                ('four_number_prize_pool_commission', models.IntegerField(default=0)),
                ('three_number_prize_pool_commission', models.IntegerField(default=0)),
                ('daily_lotto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='daily_lotto.DailyLotto', verbose_name=b'Daily Lotto')),
            ],
            options={
                'db_table': 'quotas',
            },
        ),
        migrations.AddField(
            model_name='dailylottoresult',
            name='daily_lotto_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daily_lotto.DailyLottoTicket'),
        ),
    ]
