# Generated by Django 3.0.6 on 2020-05-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lotto_api', '0010_auto_20191020_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailylottoticket',
            name='ticket_no',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
