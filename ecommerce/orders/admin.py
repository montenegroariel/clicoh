from django.contrib import admin

from .models import Order, OrderDetail


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'get_total']


class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'cuantity', 'product']


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
