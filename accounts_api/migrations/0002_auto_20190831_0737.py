# Generated by Django 2.2.4 on 2019-08-31 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuser',
            options={'ordering': ['referrals'], 'verbose_name_plural': ['users']},
        ),
        migrations.AlterModelTable(
            name='tuser',
            table='users',
        ),
    ]
