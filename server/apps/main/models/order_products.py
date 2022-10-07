from django.db import models

from server.apps.main.models import Order, Product


class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'OrderProduct'
        verbose_name_plural = 'OrderProduct'

    def __str__(self):
        return str(self.id)
