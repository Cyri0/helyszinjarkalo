from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # available = 