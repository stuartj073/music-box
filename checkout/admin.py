from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'checkout_total', 'original_basket', 'stripe_pid',)

    fields = ('order_number', 'user_profile', 'first_name',
              'surname', 'date', 'email', 'phone_number', 'street_address1',
              'street_address2', 'town_or_city', 'county', 'country',
              'postcode', 'delivery_cost', 'order_total', 'checkout_total',
              'original_basket', 'stripe_pid',)

    list_display = ('order_number', 'date', 'first_name',
                    'surname', 'order_total', 'delivery_cost',
                    'checkout_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
