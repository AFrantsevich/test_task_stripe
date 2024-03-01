import os
import stripe

from dotenv import load_dotenv
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Item


load_dotenv()


stripe.api_key = os.getenv('STRIPE_API_KEY',
                           default='sk_test_51Oo6AZG0uu3kb43DKzXsIS1m1iMzHwO'
                                   'eBlLpND175GB4htzwsnXK2rzIGxlGqa7VsDG9eAw'
                                   'ceJbpqDlyfXxsWQ7s00rAN0kdIi')


def item_info(id):
    """The function return date for create_session.
    Argument:
    price_end(id) -- Item id.
    """

    item = get_object_or_404(Item, pk=id)
    data = [
        {
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': item.name, },
                'unit_amount': item.price,
            },
            'quantity': 1,
        },
    ]
    return data


def create_session(request, id):
    domain_url = 'http://localhost:8000/'

    try:
        session = stripe.checkout.Session.create(
            line_items=item_info(id),
            mode='payment',
            success_url=domain_url + "success",
            cancel_url=domain_url + "cancelled",
        )
        return JsonResponse({'sessionId': session['id']})

    except Exception as e:
        return JsonResponse({'error': str(e)})


def buy_item(request, id):
    item = get_object_or_404(Item, pk=id)
    template = 'item_page.html'
    context = {'id': id,
               'name': item.name,
               'description': item.description,
               'price': (item.price/100), }
    return render(request, template, context)
