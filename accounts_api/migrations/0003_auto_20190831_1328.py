# Generated by Django 2.2.4 on 2019-08-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_api', '0002_auto_20190831_0737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tuser',
            options={'ordering': ['referrals'], 'verbose_name_plural': 'users'},
        ),
        migrations.AddField(
            model_name='tuser',
            name='password_reset',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
