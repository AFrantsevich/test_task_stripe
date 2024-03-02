from django.contrib import admin


from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_name', 'quantity')
    search_fields = ('get_name',)
    empty_value_display = '-пусто-'

    @admin.display(ordering='item_id__name', description='name')
    def get_name(self, obj):
        return obj.item_id.name


admin.site.register(Order, OrderAdmin)
