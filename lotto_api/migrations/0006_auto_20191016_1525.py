# Generated by Django 2.2.4 on 2019-10-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto_api', '0005_auto_20191016_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylottoticket',
            name='ticket_no',
            field=models.CharField(blank=True, default='T20191016152511eo', max_length=21, null=True, unique=True),
        ),
    ]
