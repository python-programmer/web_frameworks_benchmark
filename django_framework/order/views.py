from rest_framework.generics import ListAPIView

from .models import Order
from .serializers import OrderSerializer


class OrderListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
