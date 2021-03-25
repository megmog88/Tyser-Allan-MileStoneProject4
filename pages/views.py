from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class DrapingPageView(TemplateView):
    template_name = 'draping.html'


class LandscapingPageView(TemplateView):
    template_name = 'landscaping.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


def ContactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
