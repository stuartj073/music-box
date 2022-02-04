from django.http import HttpResponse


class StripeWH_Handler:
    """Handle webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic webhook events
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent_succeeded webhook event from stripe
        """
        intent = event.data.object
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping_details
        checkout_total = round(intent.data.charges[0].amount / 100, 2)
        
        for field, value in shipping_details.address.items():
            if value = "":
                shipping_details.address[field] = None
        
        order_exists = False
        try:
            order = Order.objects.get(
                first_name__iexact=shipping_details.name,
                last_name__iexact=shipping_details.name,
                email__iexact=billing_details.email,
                phone_number__iexact=shipping_details.phone,
                country__iexact=shipping_details.address.country,
                postcode__iexact=shipping_details.address.postal_code,
                town_or_city__iexact=shipping_details.address.city,
                street_address1__iexact=shipping_details.address.line1,
                street_address2__iexact=shipping_details.address.line2,
                county__iexact=shipping_details.address.state,
                checkout_total=checkout_total,
                original_basket=basket,
                stripe_pid=pid,
            )
            order_exists = True
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        except Order.DoesNotExist:
            try:
                order = Order.objects.create(
                    first_name__iexact=shipping_details.name,
                    last_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    checkout_total=checkout_total,
                )
                product = Product.objects.get(id=item_id)
                if isinstance(item_data, int):
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()
                else:
                    for size, quantity in item_data['items_by_size'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=quantity,
                            product_size=size,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received:{event["type"]} | ERRORL {e}',
                    status=500)
                

    
    def handle_payment_intent_failed(self, event):
        """
        Handle the payment_intent_failed webhook event from stripe
        """
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)