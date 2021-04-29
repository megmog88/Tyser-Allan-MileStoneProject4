from django.views.generic import ListView
from .models import Merchandise

# Create your views here.


class MerchandisingListView(ListView):
    model = Merchandise
    template_name = 'merchandise.html'
