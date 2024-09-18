# models.py
from django.db import models

class Title(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='title_images/')
    description = models.TextField()
    # 他のフィールドがあれば追加

    def __str__(self):
        return self.name

from django.db import models


class PilgrimageLocation(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    image = models.ImageField(upload_to='location_images/')
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

