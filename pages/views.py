from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'First_Name': form.cleaned_data['First_Name'], 
			'Surname': form.cleaned_data['Surname'], 
			'Email_Adress': form.cleaned_data['Email_Adress'], 
			'Description':form.cleaned_data['Description'],
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'Email_Adress', ['tyserallan@gmail.com'])
                messages.success(request, 'Your booking was successful!', extra_tags='alert')
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
	form = ContactForm()
	return render(request, "contact.html", {'form':form})

def submit(request):
  success = False
  success_message = " Thanks!"