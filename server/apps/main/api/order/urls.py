from django.urls import path

from server.apps.main.api.order.views.create import OrderCreate

urlpatterns = [
    path('', OrderCreate.as_view()),
]
