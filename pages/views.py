from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class DrapingPageView(TemplateView):
    template_name = 'draping.html'


class LandscapingPageView(TemplateView):
    template_name = 'landscaping.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'
