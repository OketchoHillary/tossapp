# Generated by Django 2.2.4 on 2019-09-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tossapp_api', '0002_auto_20190904_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='System_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.URLField()),
            ],
            options={
                'db_table': 'system_info',
            },
        ),
    ]
