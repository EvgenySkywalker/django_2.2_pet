from django.contrib import admin

from server.apps.main.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'order',
        'amount',
        'status',
        'payment_type',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'status',
        'payment_type',
        'created_at',
    )

    search_fields = (
        'id',
    )
