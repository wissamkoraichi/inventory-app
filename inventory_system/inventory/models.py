from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    branch_item_number = models.CharField(max_length=255)
    emco_item_number = models.CharField(max_length=255)
    emco_lot_number = models.CharField(max_length=255)
    batch_number = models.CharField(max_length=255)
    quantity_received_in_pounds = models.FloatField()

    def __str__(self):
        return f'{self.branch_item_number} - {self.emco_item_number}'
