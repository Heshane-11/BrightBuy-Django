from django.contrib import admin
from .models import Payment, Order, OrderProduct
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'quantity', 'product_price', 'ordered')
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'status', 'created_at')
    list_editable = ('status',)
    inlines = [OrderProductInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'order_{obj.id}',
            {
                'type': 'order_update',
                'status': obj.status
            }
        )


admin.site.register(Payment)
admin.site.register(OrderProduct)
