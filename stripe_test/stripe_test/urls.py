from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('stripe_app.urls',
                     namespace='stripe_app')),
    path('', include('stripe_order.urls',
                     namespace='stripe_order')),
]
