from django.db import models


   

class OrderItem(models.Model):
    order_name = models.CharField(max_length=100)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
    bitmask = models.JSONField()

    def __str__(self):
        return f"{self.order_name} - {self.product}"