from django.urls import path
from .views import DrapingListView, DrapingListInfoView

urlpatterns = [
    path('draping', DrapingListView.as_view(), name='draping'),
    path('draping/', DrapingListInfoView.as_view(), name='drapinginfo'),
]
