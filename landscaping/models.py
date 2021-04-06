from django.db import models

# Create your models here.

class Landscape(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    body = models.TextField()

    def __str__(self):
        return self.title
