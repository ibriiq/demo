# Generated by Django 3.2.8 on 2021-10-16 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userinfo_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='memos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdby_id', models.IntegerField()),
                ('memo', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'memos',
                'verbose_name_plural': 'memoss',
                'db_table': '',
                'managed': True,
            },
        ),
    ]