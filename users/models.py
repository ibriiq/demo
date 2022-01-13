from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.base import Model


from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userlevel = models.CharField(max_length=100)


class userinfo(models.Model):
    username = models.TextField()
    ip_Address = models.TextField()
    Longitude = models.TextField()
    Latitude = models.TextField()
    time = models.DateTimeField(auto_now=True)
    logout_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'userinfo'
        verbose_name_plural = 'userinfos'


