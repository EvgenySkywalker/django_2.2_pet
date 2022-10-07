from django.db import models

from server.apps.main.constants.payment import STATUS_CHOICES, STATUS_MAX_LENGTH, PAYMENT_TYPE_MAX_LENGTH, \
    PAYMENT_TYPE_CHOICES, AMOUNT_MAX_DIGITS, AMOUNT_MAX_DECIMAL_PLACES
from server.apps.main.models.order import Order


class Payment(models.Model):
    order = models.OneToOneField(Order, on_delete=models.PROTECT, related_name='payment')
    amount = models.DecimalField(max_digits=AMOUNT_MAX_DIGITS, decimal_places=AMOUNT_MAX_DECIMAL_PLACES)
    status = models.CharField(choices=STATUS_CHOICES, max_length=STATUS_MAX_LENGTH)
    payment_type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=PAYMENT_TYPE_MAX_LENGTH)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return f'[{self.payment_type}] {self.status}'
