from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Shop)
admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.FeaturedProduct)
admin.site.register(models.Review)