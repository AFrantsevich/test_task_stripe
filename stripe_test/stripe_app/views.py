import os
import stripe
import copy
from decimal import Decimal
from dotenv import load_dotenv

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Item
from stripe_order.models import Order


load_dotenv()


stripe.api_key = os.getenv('STRIPE_API_KEY',
                           default='sk_test_51Oo6AZG0uu3kb43DKzXsIS1m1iMzHwO'
                                   'eBlLpND175GB4htzwsnXK2rzIGxlGqa7VsDG9eAw'
                                   'ceJbpqDlyfXxsWQ7s00rAN0kdIi')


def index(request):
    items = Item.objects.all().order_by('pk')
    template = 'includes/index.html'
    context = {'items': items, }
    return render(request, template, context)


def item_info(id=None):
    """The function return date for create_session depends on
    the context, single item or order.
    Argument:
    price_end(id) -- Item id if we use single item.
    """
    info = {
        'price_data': {
            'currency': 'usd',
            'product_data': {'name': None},
            'unit_amount': None,
        },
        'quantity': 1,
    }
    data = []
    if id is not None:
        item = get_object_or_404(Item, pk=id)
        info['price_data']['unit_amount'] = item.price
        info['price_data']['product_data']['name'] = item.name
        data = [copy.deepcopy(info)]
    else:
        items = Order.objects.all()
        for item in items:
            info['price_data']['unit_amount'] = item.item_id.price
            info['price_data']['product_data']['name'] = item.item_id.name
            info['quantity'] = item.quantity
            data.append(copy.deepcopy(info))

    return data


def create_session(request, id=None):
    """The function create session for payment depends on
    the context, single item or order.
    Argument:
    price_end(id) -- Item id if we use single item.
    """

    domain_url = 'http://localhost/'
    try:
        session = stripe.checkout.Session.create(
            line_items=item_info(id),
            mode='payment',
            success_url=domain_url + "success/",
            cancel_url=domain_url + ("order" if not id else 'cancelled/'),
        )
        return JsonResponse({'sessionId': session['id']})

    except Exception as e:
        return JsonResponse({'error': str(e)})


def buy_item(request, id):
    """The function for buying single item,
    according to Terms of Reference.
    Argument:
    price_end(id) -- Item id if we use single item.
    """
    item = get_object_or_404(Item, pk=id)
    template = 'item_page.html'
    context = {'id': id,
               'name': item.name,
               'description': item.description,
               'price': Decimal(item.price / 100).quantize(Decimal("1.00")), }
    return render(request, template, context)
