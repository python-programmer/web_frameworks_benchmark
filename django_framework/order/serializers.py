from rest_framework.serializers import ModelSerializer

from .models import Order, OrderItem


class OrderItemSerializer(ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['id', 'product_name', 'price', 'qty']


class OrderSerializer(ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['order_number', 'order_status', 'created_at', 'total_price', 'total_qty', 'items']
