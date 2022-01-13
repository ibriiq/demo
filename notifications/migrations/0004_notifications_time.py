# Generated by Django 3.2.9 on 2022-01-12 16:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_notifications_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
