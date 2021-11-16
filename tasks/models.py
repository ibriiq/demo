from django.db import models

# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    assigned_to = models.IntegerField()
    status = models.IntegerField(default=0)
    time = models.TimeField(blank=True, null=True)
    start_timer = models.TimeField(blank=True, null=True)
    end_timer = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'tasks'
        verbose_name_plural = 'taskss'
