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
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
        return jsonify({'id': checkout_session.id})
    except Exception as e:
        return jsonify(error=str(e)), 403


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
            messages.success(request, f'Added {merchandise.name} to your bag')

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

