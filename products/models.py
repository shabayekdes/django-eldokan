from django.urls import reverse
from unicodedata import category
from django.db import models
from brands.models import Brand
from categories.models import Category


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    meta_title = models.CharField(max_length=191, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    keywords_ar = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = models.CharField(max_length=255)
    active = models.IntegerField()
    brand = models.ForeignKey(Brand, models.DO_NOTHING, blank=True, null=True)
    orders_count = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, models.DO_NOTHING, blank=True, null=True)
    optional_sub_category_id = models.IntegerField(blank=True, null=True)
    sku = models.CharField(unique=True, max_length=191, blank=True, null=True)
    discount_price = models.IntegerField(blank=True, null=True)
    discount_start_date = models.DateTimeField(blank=True, null=True)
    discount_end_date = models.DateTimeField(blank=True, null=True)
    deactivation_notes = models.TextField(blank=True, null=True)
    # creator = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    name_ar = models.CharField(max_length=255, blank=True, null=True)
    description_ar = models.TextField(blank=True, null=True)
    max_per_order = models.IntegerField(blank=True, null=True)
    min_days = models.IntegerField(blank=True, null=True)
    stock = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    long_description_ar = models.TextField(blank=True, null=True)
    long_description_en = models.TextField(blank=True, null=True)
    stock_alert = models.IntegerField(blank=True, null=True)
    barcode = models.CharField(max_length=191, blank=True, null=True)
    subtract_stock = models.IntegerField()
    order = models.IntegerField(blank=True, null=True)
    default_variant = models.IntegerField(blank=True, null=True)
    option_default_id = models.PositiveBigIntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    weight = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    has_stock = models.IntegerField(blank=True, null=True)
    preorder = models.IntegerField()
    preorder_price = models.IntegerField(blank=True, null=True)
    preorder_start_date = models.DateTimeField(blank=True, null=True)
    preorder_end_date = models.DateTimeField(blank=True, null=True)
    video = models.CharField(max_length=191, blank=True, null=True)
    available_soon = models.IntegerField()
    bundle_checkout = models.IntegerField()
    meta_title_ar = models.TextField(blank=True, null=True)
    meta_description_ar = models.TextField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    downloadable_url = models.CharField(max_length=191, blank=True, null=True)
    downloadable_url_ar = models.CharField(max_length=191, blank=True, null=True)
    downloadable_label = models.CharField(max_length=191, blank=True, null=True)
    downloadable_label_ar = models.CharField(max_length=191, blank=True, null=True)
    affiliate_commission = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    featured = models.IntegerField()
    free_delivery = models.IntegerField()
    exclusive_price = models.IntegerField(blank=True, null=True)
    primary_option = models.PositiveBigIntegerField(blank=True, null=True)
    video_url = models.CharField(max_length=191, blank=True, null=True)
    video_thumbnail_url = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        db_table = 'products'

    def get_absolute_url(self):
        return reverse("products-detail", kwargs={"id": self.pk})

    def __str__(self):
        return self.name
