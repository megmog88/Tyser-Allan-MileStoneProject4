from django.urls import path
from .views import MerchandiseListView, MerchandiseDetailView

urlpatterns = [
    path('merchandise', MerchandiseListView.as_view(), name='merchandise'),
    path('merchandises/<int:pk>/', MerchandiseDetailView.as_view(), name='merchandiseinfo'),
]
