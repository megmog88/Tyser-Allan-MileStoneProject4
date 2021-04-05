from django.urls import path
from .views import DrapingListView

urlpatterns = [
    path('draping', DrapingListView.as_view(), name='draping'),
]
