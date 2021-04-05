from django.views.generic import ListView, DetailView
from .models import Drape

# Create your views here.


class DrapingListView(ListView):
    model = Drape
    template_name = 'draping.html'


class DrapingDetailView(DetailView):
    model = Drape
    template_name = 'drapinginfo.html'
