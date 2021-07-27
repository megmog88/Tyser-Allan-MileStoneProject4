from django.shortcuts import render, redirect, reverse
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpRequest
from django.views import View
from merchandise.models import Merchandise
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

stripe.api_key = 'sk_test_51J0z9rGPlg2qv8pjSe6AaOP3N618aC0yFl6C1XeOrpsK9rhR55lqbm2EPuxlknpKQluo4BpHW4qiey97Vs3mpVBw00DRG6QXjX'

YOUR_DOMAIN = 'http://localhost:4242'

@login_required
def create_checkout_session(request: HttpRequest):
 
    customer = ... # get customer model based off request.user
 
    if request.method == 'POST':
 
        # Set Stripe API key
        stripe.api_key = settings.STRIPE_SECRET_KEY
 
        # Create Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            mode="subscription",
            success_url=f"https://tyser-allan.herokuapp.com/payment/success?sessid={{CHECKOUT_SESSION_ID}}",
            cancel_url=f"https://tyser-allan.herokuapp.com/payment/cancel", # The cancel_url is typically set to the original product page
        )
 
    return JsonResponse({'sessionId': checkout_session['id']})


@login_required
def view_shoppingbag(request):
    """ A view that renders the guests shopping bag """

    return render(request, 'shoppingbag/shoppingbag.html')

@login_required
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

@login_required
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

endpoint_secret = 'whsec_8OSztSqQWtSHesWexLjClViw3TMIW9pj'


def my_webhook_view(request):
  payload = request.body
  sig_header = request.META['HTTP_STRIPE_SIGNATURE']
  event = None

  try:
    event = stripe.Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  except ValueError as e:
    # Invalid payload
    return HttpResponse(status=400)
  except stripe.error.SignatureVerificationError as e:
    # Invalid signature
    return HttpResponse(status=400)

  # Handle the checkout.session.completed event
  if event['type'] == 'checkout.session.completed':
    session = event['data']['object']

    line_items = stripe.checkout.Session.list_line_items(session['id'], limit=100)

    # Fulfill the purchase...
    try:
      fulfill_order(session, line_items)
    except NotImplementedError as e:
      return HttpResponse(status=400)

  # Passed signature verification
  return HttpResponse(status=200)

def fulfill_order(session, line_items):
  # TODO: Remove error and implement...
  raise NotImplementedError("Given the Checkout Session \"" + session['id'] + "\", load your internal order from the database here.\nThen you can reconcile your order's quantities with the final line item quantity purchased.\nYou can use `checkout_session.metadata` and `price.metadata` to store and later reference your internal order and item ids.")
