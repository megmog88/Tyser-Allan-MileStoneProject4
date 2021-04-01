from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class DrapingPageView(TemplateView):
    template_name = 'draping.html'
