from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    photo = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return self.username
