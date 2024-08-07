# Generated by Django 5.0.6 on 2024-07-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_location_product_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='barcode',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]