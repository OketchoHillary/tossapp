# Generated by Django 2.2.4 on 2019-09-04 07:01

from django.db import migrations, models
import tossapp_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('tossapp_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='display_photo',
            field=models.ImageField(default='games/Daily_lotto.jpg', upload_to=tossapp_api.models.content_file_name),
        ),
    ]