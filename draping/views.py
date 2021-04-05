from django.views.generic import ListView
from .models import Drape

# Create your views here.


class DrapeListView(ListView):
    model = Drape
    template_Name = 'draping.html'
