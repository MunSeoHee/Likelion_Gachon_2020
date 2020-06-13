from django.db import models

class User(models.Model):
    email = models.CharField(max_length=100)
    pw = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    gender = models.BooleanField()
    age = models.IntegerField()

    def __str__(self):
        return self.email
# Create your models here.
