# Generated by Django 3.2.9 on 2021-11-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='tax_renewed_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]