from django.urls import include, path

from server.apps.main.api.order import urls as order_urls
from server.apps.main.api.product import urls as product_urls
from server.apps.main.api.payment import urls as payment_urls

urlpatterns = [
    path('order/', include(order_urls)),
    path('product/', include(product_urls)),
    path('payment/', include(payment_urls)),
]
