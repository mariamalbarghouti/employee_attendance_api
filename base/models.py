from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)

class ImageModel(models.Model):
    # name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class ImageComparisonModel(models.Model):
    person = models.ImageField()

