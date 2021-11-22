# Generated by Django 3.2.9 on 2021-11-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_cars_tax_renewed_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('is_checked', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'checklist_cars',
                'verbose_name_plural': 'checklist_cars',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='cars',
            name='tax_renewed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
