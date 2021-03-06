# Generated by Django 3.2.9 on 2022-01-12 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_by', models.IntegerField()),
                ('time', models.DateField()),
                ('purpose', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('approved_by', models.IntegerField(blank=True)),
                ('assigned_to', models.IntegerField(blank=True)),
            ],
            options={
                'verbose_name': 'Car_request',
                'verbose_name_plural': 'Car_requests',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
