from django.urls import path
from .views import MerchandisingListView

urlpatterns = [
    path('merchandise', MerchandisingListView.as_view(), name='merchandise'),
]
