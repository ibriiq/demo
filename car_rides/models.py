from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Car_request(models.Model):
    requested_by = models.IntegerField() #models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.DateField(auto_now=False, auto_now_add=False)
    purpose = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField(blank=True, null=True)
    rejected_by = models.IntegerField(blank=True, null=True)
    rejected_reason = models.TextField(blank=True, null=True)
    approved_by = models.IntegerField(blank=True, null=True) #models.ForeignKey(User, on_delete=models.DO_NOTHING)
    assigned_to = models.IntegerField(blank=True, null=True) #models.ForeignKey(User, on_delete=models.DO_NOTHING)
    

    def __str__(self):
        return self.purpose

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Car_request'
        verbose_name_plural = 'Car_requests'