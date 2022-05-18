from django.db import models

# Create your models here.
class Brand(models.Model):
    name_en = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
