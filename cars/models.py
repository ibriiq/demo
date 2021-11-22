from django.db import models

# Create your models here.

class Cars(models.Model):
    car_type = models.CharField(max_length=250)
    assigned_to = models.IntegerField()
    tax_renewed_date = models.DateField(blank=True, null=True,)
    tax_expiration_date = models.DateField(blank=True, null=True)
    fitness_renewed_date = models.DateField(blank=True, null=True)
    fitness_expiration_date = models.DateField(blank=True, null=True)
    car_maintanance_date = models.DateField(blank=True, null=True)
    car_condition = models.CharField(max_length=250, blank=True, null=True)



    def __str__(self):
        return self.car_type

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'cars'
        verbose_name_plural = 'carss'


class Checklist_car(models.Model):
    car_id = models.IntegerField()
    title = models.CharField(max_length=250)
    is_checked = models.IntegerField(default=0)



    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'checklist_cars'
        verbose_name_plural = 'checklist_cars'