from django.views.generic import ListView, DetailView, TemplateView
from .models import Merchandise

# Create your views here.


class MerchandiseListView(ListView):
    model = Merchandise
    template_name = 'merchandise.html'

class MerchandiseDetailView(DetailView):
    model = Merchandise
    template_name = 'merchandiseinfo.html'

