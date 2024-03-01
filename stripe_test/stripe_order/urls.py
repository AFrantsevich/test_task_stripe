from django.urls import path

from . import views


app_name = 'stripe_order'


urlpatterns = [
    path('add/', views.add_to_order, name='add_to_order'),
    path('order/', views.order, name='order'),
    path('update_order_item/', views.update_order_item,
         name='update_order_item'),
]
