# Generated by Django 4.2.10 on 2024-02-26 08:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import ishop.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(1)])),
                ('quantity', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ishop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(help_text='Enter the phone number without spaces or special characters, e.g., 03012345678', max_length=11)),
                ('website', models.URLField(blank=True, help_text='Enter the URL starting with http:// or https://', null=True)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 star'), (2, '2 star'), (3, '3 star'), (4, '4 star'), (5, '5 star')])),
                ('comment', models.TextField(blank=True, max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='ishop.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='ishop.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ishop.shop'),
        ),
        migrations.CreateModel(
            name='FeaturedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(default=ishop.models.default_end_date)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='is_featured', to='ishop.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_products', to='ishop.shop')),
            ],
        ),
    ]
