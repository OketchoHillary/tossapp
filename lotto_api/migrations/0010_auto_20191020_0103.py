# Generated by Django 2.2.4 on 2019-10-19 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto_api', '0009_auto_20191016_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylotto',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
