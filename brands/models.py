from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    featured = models.IntegerField()
    active = models.IntegerField()

    class Meta:
        db_table = 'brands'
