from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)
    name_ar = models.CharField(max_length=50, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    featured = models.BooleanField()
    active = models.BooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'brands'
