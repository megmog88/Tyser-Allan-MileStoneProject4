from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Merchandise


def shoppingbag_contents(request):

    shoppingbag_items = []
    total = 0
    merchandise_count = 0
    shoppingbag = request.session.get('shoppingbag', {})

    for item_id, quantity in shoppingbag.items():
        merchandise = get_object_or_404(Merchandise, pk=item_id)
        total += quantity * merchandise.price
        merchandise_count += quantity
        shoppingbag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'merchandise': merchandise,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'shoppingbag_items': shoppingbag_items,
        'total': total,
        'merchandise_count': merchandise_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
