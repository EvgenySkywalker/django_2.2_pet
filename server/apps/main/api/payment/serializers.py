from rest_framework import serializers
from rest_framework.exceptions import NotFound

from server.apps.main.models import Order, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class PaymentWriteSerializer(serializers.ModelSerializer):
    order_uid = serializers.CharField()

    class Meta:
        model = Payment
        fields = ('order_uid', 'status', 'payment_type')

    def create(self, validated_data) -> Payment:
        order_uid = validated_data['order_uid']
        order = Order.objects.only('total_amount').filter(uid=order_uid).first()
        if order is None:
            raise NotFound(f'Сant find order with given ID: {order_uid}')

        return Payment.objects.create(
            order_id=order.id,
            amount=order.total_amount,
            status=validated_data['status'],
            payment_type=validated_data['payment_type'],
        )
