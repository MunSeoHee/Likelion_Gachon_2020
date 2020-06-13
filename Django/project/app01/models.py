from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField()

    def __str__(self):
        return self.title
# Create your models here.
