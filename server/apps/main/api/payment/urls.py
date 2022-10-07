from django.urls import path

from server.apps.main.api.payment.views.create import PaymentCreate

urlpatterns = [
    path('', PaymentCreate.as_view()),
]
