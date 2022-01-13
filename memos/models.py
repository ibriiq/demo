from django.db import models

# Create your models here.


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
        verbose_name_plural = 'memos'