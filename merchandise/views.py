from django.views.generic import ListView, DetailView, TemplateView
from .models import Merchandise
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.


class MerchandiseListView(ListView):
    model = Merchandise
    template_name = 'merchandise.html'

class MerchandiseDetailView(DetailView):
    model = Merchandise
    template_name = 'merchandiseinfo.html'

