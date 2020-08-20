from django.db import models
from django.db.models import F, FloatField, ExpressionWrapper


class Order(models.Model):
    INIT = 0
    IN_PROGRESS = 1
    DONE = 2
    ORDER_STATUS = [
        (INIT, 'initiate'),
        (IN_PROGRESS, 'in progress'),
        (DONE, 'done')
    ]

    order_number = models.IntegerField(primary_key=True)
    order_status = models.PositiveSmallIntegerField(choices=ORDER_STATUS, default=INIT)
    created_at = models.DateTimeField()

    class Meta:
        ordering = ('-order_number',)

    def __str__(self):
        return 'order {0}'.format(self.order_number)

    def total_price(self):
        return self.items\
            .annotate(total_price=ExpressionWrapper(F('qty') * F('price'), output_field=FloatField()))\
            .aggregate(models.Sum('total_price'))['total_price__sum']

    def total_qty(self):
        return self.items.aggregate(models.Sum('qty'))['qty__sum']


class OrderItem(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField(default=0)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}: {1} X {2}'.format(self.product_name, self.price, self.qty)

    def total_price(self):
        return self.qty * self.price
