from django.contrib import admin
from .models import Product


# Register your models here.
class VariantProductInline(admin.StackedInline):
    model = Product


class ProductAdmin(admin.ModelAdmin):
    inlines = [VariantProductInline]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.exclude(parent__isnull=False)


admin.site.register(Product, ProductAdmin)
