from drf_rw_serializers import generics
from drf_yasg.utils import swagger_auto_schema

from server.apps.main.api.payment.serializers import PaymentWriteSerializer, PaymentSerializer


class PaymentCreate(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    write_serializer_class = PaymentWriteSerializer

    @swagger_auto_schema(request_body=write_serializer_class, responses={201: serializer_class()})
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
