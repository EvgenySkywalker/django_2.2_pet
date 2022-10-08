import requests
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse, path
from django.utils.html import format_html
from django.utils.timezone import now

from server.apps.main.admin.inlines import OrderProductInline
from server.apps.main.models import Order, OrderProduct, Product


def approve_view(request, object_id):
    instance = Order.objects.get(id=object_id)
    product_ids = OrderProduct.objects.filter(order_id=instance.id).values_list('product__id')
    print(product_ids)
    products = Product.objects.filter(id__in=product_ids).all()
    total_amount = sum(product.price for product in products)
    if total_amount != instance.total_amount:
        raise ValidationError(f'Total amount has changed before={instance.total_amount}, now={total_amount}')
    instance.status = 'approved'
    #instance.approved_at = localtime()
    # Выполнял задание на windows, из-за проблем с докером не смог поставить USE_TZ=True, поэтому как есть (
    instance.approved_at = now()
    instance.save()
    response = requests.post(
        'https://webhook.site/36693e00-8f59-4f7b-9a85-1d1e7ddde4d4',
        json={
            'id': str(instance.uid),
            'amount': str(instance.total_amount),
            'date': instance.approved_at.isoformat(),
        },
    )
    print(response.status_code)
    return HttpResponseRedirect(redirect_to='/admin/main/order/')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'total_amount',
        'status',
        'payment',
        'approve',
        'uid',
        'approved_at',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'status',
        'approved_at',
        'created_at',
    )

    search_fields = (
        'id',
        'uid',
    )

    list_select_related = (
        'payment',
    )

    inlines = [OrderProductInline]

    def get_urls(self):
        view_name = '{}_{}_approve'.format(self.model._meta.app_label, self.model._meta.model_name)
        return [path('<path:object_id>/approve/', approve_view, name=view_name)] + super().get_urls()

    def approve(self, obj):
        # не смог решить что лучше, указать индексами или литералами, остановился на последнем
        if obj.payment is None or obj.payment.status != 'success' or obj.status == 'approved':
            return '-'
        view_name = "admin:{}_{}_approve".format(obj._meta.app_label, obj._meta.model_name)
        link = reverse(view_name, args=[obj.pk])
        html = '<input type="button" onclick="location.href=\'{}\'" value="Подтвердить" />'.format(link)
        return format_html(html)
