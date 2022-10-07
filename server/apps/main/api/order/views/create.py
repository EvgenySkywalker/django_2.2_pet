from drf_rw_serializers import generics
from drf_yasg.utils import swagger_auto_schema

from server.apps.main.api.order.serializers import OrderWriteSerializer, OrderSerializer


class OrderCreate(generics.CreateAPIView):
    serializer_class = OrderSerializer
    write_serializer_class = OrderWriteSerializer

    @swagger_auto_schema(request_body=write_serializer_class)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
