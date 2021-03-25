from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class DrapingPageView(TemplateView):
    template_name = 'draping.html'


class LandscapingPageView(TemplateView):
    template_name = 'landscaping.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'first_name': form.cleaned_data['first_name'],
            'last_name': form.cleaned_data['last_name'],
            'email': form.cleaned_data['email_address'],
            'message':form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                return redirect('home')

    form = ContactForm()
    return render(request, "contact.html", {'form':form})
