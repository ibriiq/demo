# Generated by Django 3.2.9 on 2021-11-16 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20211116_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='time',
            field=models.TimeField(default=0),
        ),
    ]
