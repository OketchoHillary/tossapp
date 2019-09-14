# Generated by Django 2.2.4 on 2019-08-31 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0003_auto_20190831_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuser',
            name='password_reset',
        ),
        migrations.CreateModel(
            name='Reset_password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password_reset', models.CharField(blank=True, max_length=8, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]