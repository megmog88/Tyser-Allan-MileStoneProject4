from django.shortcuts import render, redirect, reverse
import stripe
from django.conf import settings
from django.http import JsonResponse, HttpRequest
from django.views import View
from merchandise.models import Merchandise
from django.views.generic import TemplateView

# Create your views here.

stripe.api_key = settings.STRIPE_SECRET_KEY

def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=0,
            currency='gbp',
            description='Tyser&Allan Charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


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

