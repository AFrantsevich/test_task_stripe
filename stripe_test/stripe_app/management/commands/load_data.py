import random

from django.core.management import BaseCommand

from django_seed import Seed

from stripe_app.models import Item


class Command(BaseCommand):
    name = 'SEED'

    def __init__(self):
        BaseCommand.__init__(self)
        self.seeder = Seed.seeder()

    def __seed_item(self, seeder, amount_items, price_start, price_end):
        """The function populates the database's table 'Item'
        with random Items.
        Argument:
        amount_items(int) -- amount of Items to be added to DB.
        price_start(int) -- random price starts this.
        price_end(int) -- random price ends this.
        """
        for i in range(1, amount_items + 1):
            seeder.add_entity(Item, 1, {
                'name': f'{i} Item',
                'description': f'This is description of Item number {i}',
                'price': random.randint(price_start, price_end)
            })
        seeder.execute()

    def add_arguments(self, parser):
        parser.add_argument('amount_items', type=int,
                            help='Amount of Items to be added to DB')
        parser.add_argument('price_start', type=int,
                            help='Random price starts this')
        parser.add_argument('price_end', type=int,
                            help='Random price ends this')

    def handle(self, *args, **kwargs):
        amount_items = kwargs['amount_items']
        price_start = kwargs['price_start']
        price_end = kwargs['price_end']

        self.__seed_item(self.seeder, amount_items, price_start, price_end)
