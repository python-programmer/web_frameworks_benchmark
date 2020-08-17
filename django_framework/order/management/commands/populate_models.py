import json
from django.core.management import BaseCommand

from order.models import OrderItem, Order


class Command(BaseCommand):
    help = 'populate Order and OrderItem modes'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options['filename']

        with open(filename) as json_file:
            data = json.load(json_file)
            for order in data:
                order_item_list = order.pop('items')

                order_saved = Order.objects.create(**order)

                order_item_model_list = []
                for item in order_item_list:
                    item['order_id'] = order_saved.order_number
                    order_item = OrderItem(**item)
                    order_item_model_list.append(order_item)

                order_saved.items.bulk_create(order_item_model_list)
