from rest_framework import mixins, generics
from server.apps.main.api.product.filters import ProductFilter
from server.apps.main.api.product.serializers import ProductSerializer
from server.apps.main.models import Product


class ProductList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
