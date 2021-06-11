from django.shortcuts import render, redirect, reverse
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpRequest
from django.views import View
from merchandise.models import Merchandise
from django.views.generic import TemplateView

# Create your views here.


def view_shoppingbag(request):
    """ A view that renders the guests shopping bag """

    return render(request, 'shoppingbag/shoppingbag.html')


def add_to_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'merchandise_size' in request.POST:
        size = request.POST['merchandise_size']
    shoppingbag = request.session.get('shoppingbag', {})

    if size:
        if item_id in list(shoppingbag.keys()):
            if size in shoppingbag[item_id]['items_by_size'].keys():
                shoppingbag[item_id]['items_by_size'][size] += quantity
            else:
                shoppingbag[item_id]['items_by_size'][size] = quantity
        else:
            shoppingbag[item_id] = {'items_by_size': {size: quantity}}
    else:
        if item_id in list(shoppingbag.keys()):
            shoppingbag[item_id] += quantity
        else:
            shoppingbag[item_id] = quantity

    request.session['shoppingbag'] = shoppingbag
    return redirect(redirect_url)


def modify_shoppingbag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'merchandise_size' in request.POST:
        size = request.POST['merchandise_size']
    shoppingbag = request.session.get('shoppingbag', {})
    if size: 
        if quantity > 0:
            shoppingbag[item_id]['items_by_size'][size] = quantity
        else:
            del shoppingbag[item_id]['items_by_size'][size]
    else:
        if quantity > 0:
            shoppingbag[item_id] = quantity
        else:
            shoppingbag.pop[item_id]


    request.session['shoppingbag'] = shoppingbag
    return redirect(reverse('view_shoppingbag'))

def remove_shoppingbag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        size = None
        if 'merchandise_size' in request.POST:
            size = request.POST['merchandise_size']
        shoppingbag = request.session.get('shoppingbag', {})

        if size:
            del shoppingbag[item_id]['items_by_size'][size]
            if not shoppingbag[item_id]['items_by_size']:
                shoppingbag.pop(item_id)
        else:
            shoppingbag.pop(item_id)

        request.session['shoppingbag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

def create_checkout_session(request: HttpRequest):
 
    customer = ... # get customer model based off request.user
 
    if request.method == 'POST':
 
        # Assign product price_id, to support multiple products you 
        # can include a product indicator in the incoming POST data
        price_id = ...
 
        # Set Stripe API key
        stripe.api_key = settings.STRIPE_SECRET_KEY
 
        # Create Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            line_items=[
                {
                    "price": price_id,
                    "quantity": 1
                }
            ],
            customer=customer.id,
            success_url=f"https://YOURDOMAIN.com/payment/success?sessid={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"https://YOURDOMAIN.com/payment/cancel", # The cancel_url is typically set to the original product page
        )
 
    return JsonResponse({'sessionId': checkout_session['id']})


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"

class MerchandiseLandingPageView(TemplateView):
    template_name = "merchandise.html"

    def get_context_data(self, **kwargs):
        merchandise = Merchandise.objects
        context = super(MerchandiseLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "merchandise": merchandise,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context