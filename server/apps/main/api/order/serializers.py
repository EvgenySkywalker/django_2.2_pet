from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import NotFound

from server.apps.main.constants.order import STATUS_CREATED
from server.apps.main.models import Order, Product, OrderProduct


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderWriteSerializer(serializers.ModelSerializer):
    product_uids = serializers.ListField(child=serializers.UUIDField(), allow_empty=False)

    class Meta:
        model = Order
        fields = ('product_uids',)

    def create(self, validated_data) -> Order:
        product_uids = set(validated_data['product_uids'])
        products = Product.objects.filter(uid__in=product_uids).all()
        unknown_products = product_uids - set(product.uid for product in products)
        if unknown_products:
            raise NotFound(f'Can`t find products {unknown_products}')
        with transaction.atomic():
            order = Order.objects.create(
                status=STATUS_CREATED,
                total_amount=sum(product.price for product in products),
            )
            order_product_list = [OrderProduct(order_id=order.id, product_id=product.id) for product in products]
            OrderProduct.objects.bulk_create(order_product_list, ignore_conflicts=True)
        return order
