from django.db import models
from django.utils import timezone

from accounts.models import CustomUser

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=11, help_text='Enter the phone number without spaces or special characters, e.g., 03012345678')
    website = models.URLField(null=True, blank=True, help_text='Enter the URL starting with http:// or https://')
    owner = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='shop')

    # rating = models.FloatField()
    # featured_products = models.ForeignKey(Product)
    # reviews = models.ForeignKey(Review))
    # tags = models.ManyToManyField(Tag)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')


class ProductImage(models.Model):
    image = models.ImageField(upload_to='product_images/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')


class FeaturedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='is_featured')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='featured_products')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=lambda: timezone.now() + timezone.timedelta(days=7))

    @property
    def is_active(self):
        now = timezone.now()
        return self.start_date <= now < self.end_date

    def __str__(self):
        return self.is_active