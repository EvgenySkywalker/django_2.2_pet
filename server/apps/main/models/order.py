import uuid

from django.db import models

from server.apps.main.constants.order import STATUS_MAX_LENGTH, TOTAL_MAX_DECIMAL_PLACES, TOTAL_MAX_DIGITS, \
    STATUS_CHOICES, STATUS_APPROVED


class Order(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=STATUS_MAX_LENGTH)
    total_amount = models.DecimalField(max_digits=TOTAL_MAX_DIGITS, decimal_places=TOTAL_MAX_DECIMAL_PLACES)
    approved_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        constraints = [
            models.CheckConstraint(
                check=models.Q(
                    models.Q(status=STATUS_APPROVED) & models.Q(approved_at__isnull=False) & models.Q(payment__isnull=False) |
                    ~models.Q(status=STATUS_APPROVED) & models.Q(approved_at__isnull=True)
                ),
                name='main_order_approved_at_only_for_approved',
            ),
        ]

    def __str__(self):
        return str(self.id)
