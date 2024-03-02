from stripe_app.models import Item
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse

from .models import Order


def add_to_order(request):
    id_item = request.GET.get('id', None)
    quantity = request.GET.get('quantity', None)

    try:
        if int(quantity) == 0 or int(quantity) < 0:
            return redirect('stripe_order:order')

        if id_item and quantity:
            item = get_object_or_404(Item, pk=id_item)
            order = Order.objects.filter(item_id=item)

            if order:
                order = order.get()
                order.quantity = quantity
                order.save()
            else:
                Order.objects.get_or_create(
                    item_id=item,
                    quantity=quantity
                )
            return redirect('stripe_order:order')

    except Exception as e:
        return JsonResponse({'error': str(e)})


def order(request):
    items = Order.objects.all()
    template = 'includes/order.html'
    context = {'cart_items': items}
    return render(request, template, context)


def update_order_item(request):
    id_item = request.GET.get('id', None)
    new_quantity = request.GET.get('quantity', None)

    try:
        if id_item and new_quantity:
            changeable_order = get_object_or_404(Order, item_id=id_item)
            if int(new_quantity) == 0 or int(new_quantity) < 0:
                changeable_order.delete()
                return redirect('stripe_order:order')

            changeable_order.quantity = new_quantity
            changeable_order.save()

            return JsonResponse({'success': True,
                                 'cart_item_total_price':
                                     get_object_or_404(
                                         Order,
                                         item_id=id_item).item_total_price,
                                 'order_total_price':
                                     get_object_or_404(
                                         Order,
                                         item_id=id_item).order_total_price},
                                status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)})
