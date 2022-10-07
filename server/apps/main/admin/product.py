from django.contrib import admin

from server.apps.main.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'image',
        'content',
        'price',
    )

    list_display = (
        'id',
        'uid',
        'name',
        'image',
        'content',
        'price',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'id',
        'name',
    )
