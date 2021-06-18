from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from django.conf import settings


def index(request):
    return render(request, 'index.html', {'site_key': settings.RECAPTCHA_SITE_KEY})

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


def ContactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            First_Name = form.cleaned_data['First_Name']
            Email_Adress = form.cleaned_data['Email_Adress']
            Description = form.cleaned_data['Description']
            try:
                send_mail('Tyser&Allan', 'Thank you for your email, we will get back to you as soon as possible', 
                'EMAIL_HOST_USER', ['to@example.com'],
    fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
