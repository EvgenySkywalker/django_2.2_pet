import uuid

from django.db import models

from server.apps.main.constants.product import NAME_MAX_LENGTH, CONTENT_MAX_LENGTH, PRICE_MAX_DECIMAL_PLACES, PRICE_MAX_DIGITS


class Product(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    image = models.ImageField(height_field='image_height', width_field='image_width')
    image_height = models.IntegerField(blank=True, null=True)
    image_width = models.IntegerField(blank=True, null=True)
    content = models.TextField(max_length=CONTENT_MAX_LENGTH, blank=True, null=True)
    price = models.DecimalField(max_digits=PRICE_MAX_DIGITS, decimal_places=PRICE_MAX_DECIMAL_PLACES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'[{self.id}] {self.name}'
