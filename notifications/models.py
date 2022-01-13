from django.db import models

# Create your models here.

class notifications(models.Model):
    userid = models.IntegerField()
    notification = models.CharField(max_length=255)
    notification_type = models.IntegerField()
    task_id = models.IntegerField(default=0)
    time = models.DateTimeField()
    status = models.CharField(max_length=255, default="New")

    def __str__(self):
        return self.notification

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'notifications'
        verbose_name_plural = 'notificationss'