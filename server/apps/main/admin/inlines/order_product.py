from django.contrib import admin

from server.apps.main.models import OrderProduct


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
