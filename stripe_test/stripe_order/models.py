from decimal import Decimal

from django.db import models
from stripe_app.models import Item


class Order(models.Model):
    item_id = models.ForeignKey(
        Item, null=True,
        on_delete=models.SET_NULL,
        related_name='items'
    )
    quantity = models.IntegerField()

    @property
    def item_total_price(self):
        total_price = self.quantity * self.item_id.price
        return Decimal(total_price / 100).quantize(Decimal("1.00"))

    @property
    def order_total_price(self):
        total_price = (
            sum(item.item_total_price for item in Order.objects.all()))
        return Decimal(total_price.quantize(Decimal("1.00")))

    @property
    def amount_items(self):
        amount_items = len(Order.objects.all())
        return amount_items

    class Meta:
        ordering = ['item_id__name']
