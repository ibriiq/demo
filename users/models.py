from django.db import models
# Create your models here.

class userinfo(models.Model):
    username = models.TextField()
    ip_Address = models.TextField()
    Longitude = models.TextField()
    Latitude = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'userinfo'
        verbose_name_plural = 'userinfos'