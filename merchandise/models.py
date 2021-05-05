from django.db import models

# Create your models here.


class Merchandise(models.Model):
    title = models.CharField(max_length=200)
    cover = models.ImageField('media/images/')
    description = models.TextField()
    different_sizes = models.BooleanField(default=False, null=False, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
