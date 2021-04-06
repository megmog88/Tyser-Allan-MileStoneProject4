from django.views.generic import ListView, DetailView
from .models import Landscape

# Create your views here.


class LandscapingListView(ListView):
    model = Landscape
    template_name = 'landscaping.html'


class LandscapingDetailView(DetailView):
    model = Landscape
    template_name = 'landscapinginfo.html'
