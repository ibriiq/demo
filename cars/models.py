from django.db import models

# Create your models here.

class Cars(models.Model):
    car_type = models.CharField(max_length=250)
    assigned_to = models.IntegerField()

    def __str__(self):
        return self.car_type

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'cars'
        verbose_name_plural = 'carss'