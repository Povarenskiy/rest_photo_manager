from django.db import models
from django.conf import settings


class Names(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
        

class Photo(models.Model):
    image_url = models.ImageField(upload_to='uploads/', blank=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(max_length=255, blank=True)
    people = models.ManyToManyField(Names, blank=True)
    country = models.TextField(max_length=100, blank=True)
    city = models.TextField(max_length=100, blank=True)
