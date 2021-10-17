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


class memos(models.Model):
    createdby_id = models.IntegerField()
    memo = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
                return self.memo


    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'memos'
        verbose_name_plural = 'memoss'