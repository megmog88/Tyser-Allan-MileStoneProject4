from django.urls import path
from .views import DrapingListView, DrapingDetailView

urlpatterns = [
    path('draping', DrapingListView.as_view(), name='draping'),
    path('drapes/<int:pk>/', DrapingDetailView.as_view(), name='drapinginfo'),
]
