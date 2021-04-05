from django.views.generic import ListView
from .models import Drape

# Create your views here.


class DrapingListView(ListView):
    model = Drape
    template_name = 'draping.html'
