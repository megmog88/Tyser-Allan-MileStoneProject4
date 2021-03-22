from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class MerchandisePageView(TemplateView):
    template_name = 'merchandise.html'


class LogInPageView(TemplateView):
    template_name = 'login.html'


class SignUpPageView(TemplateView):
    template_name = 'sigup.html'
