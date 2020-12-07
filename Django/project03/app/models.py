from django.db import models

# Create your models here.
class Blog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    contents = models.TextField()