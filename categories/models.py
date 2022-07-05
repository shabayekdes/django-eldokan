from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description_ar = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    deactivation_notes = models.TextField(blank=True, null=True)
    order = models.IntegerField()
    slug = models.SlugField()
    is_highlighter = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'categories'
