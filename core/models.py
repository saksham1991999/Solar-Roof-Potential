from django.db import models


class Rooftop(models.Model):
    image = models.ImageField()
    area = models.FloatField(blank=True, null=True)
    energy = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
