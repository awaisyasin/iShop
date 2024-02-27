# Generated by Django 4.2.10 on 2024-02-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ishop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='username',
            field=models.CharField(help_text='Enter a unique username for the shop. This will be used for identification.', max_length=255, unique=True),
        ),
    ]