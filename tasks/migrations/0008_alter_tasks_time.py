# Generated by Django 3.2.9 on 2021-11-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_alter_tasks_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]