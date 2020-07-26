from django.db import models

# Create your models here.
class list(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()