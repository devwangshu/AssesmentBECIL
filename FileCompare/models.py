from django.db import models




class AnimalFood(models.Model):
    name = models.ImageField(upload_to='image/', null=True, blank=True)
    food = models.ImageField(upload_to='image/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
