from django.urls import path
from .views import MerchandiseListView, MerchandiseDetailView
from . import views

urlpatterns = [
    path('merchandise', MerchandiseListView.as_view(), name='merchandise'),
    path('merchandise/<int:pk>/', MerchandiseDetailView.as_view(), name='merchandise'),
]
