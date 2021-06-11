import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from merchandise.models import Merchandise
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        merchandise_id = self.kwargs["pk"]
        merchandise= Merchandise.objects.get(id=merchandise_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': merchandise.price,
                        'product_data': {
                            'name': merchandise.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "merchandise_id": merchandise.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"

class MerchandiseLandingPageView(TemplateView):
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        merchandise = Merchandise.objects.get(name="Test Product")
        context = super(MerchandiseLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "merchandise": merchandise,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context