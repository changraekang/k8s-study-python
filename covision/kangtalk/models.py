from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.CharField(unique=True, max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_use = models.IntegerField(blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    expired = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'