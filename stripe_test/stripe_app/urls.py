from django.urls import path
from django.views.generic.base import TemplateView

from . import views


app_name = 'stripe_app'


urlpatterns = [
    path('buy/<int:id>', views.create_session, name='create_session'),
    path('item/<int:id>', views.buy_item, name='buy_item'),
    path('success', TemplateView.as_view(template_name='success.html'),
         name='success'),
    path('cancelled', TemplateView.as_view(template_name='cancelled.html'),
         name='cancelled'),
]
