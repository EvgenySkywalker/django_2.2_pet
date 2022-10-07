from django.urls import path

from server.apps.main.api.product.views.list import ProductList

urlpatterns = [
    path('', ProductList.as_view()),
]
