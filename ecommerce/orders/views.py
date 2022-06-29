from django.db.models import F
from products.models import Product
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Order, OrderDetail
from .serializers import OrderDetailSerializer, OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def destroy(self, request, *args, **kwargs):
       order = self.get_object()
       order_detail = OrderDetail.objects.filter(order=order)
       for detail in order_detail:
           Product.objects.filter(pk=detail.product.id).update(stock = F('stock') + detail.cuantity)
       return super(OrderViewSet, self).destroy(request, *args, **kwargs)


class OrderDetailViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
