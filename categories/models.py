from pydoc import describe
from django.db import models

# Create your models here.
class Category(models.Model):
    name_en = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50)
    description_en = models.TextField()
    description_ar = models.TextField()
    slug = models.CharField(unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
