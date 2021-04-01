from django.urls import path, include
from .views import DrapingPageView

urlpatterns = [
    path('draping', DrapingPageView.as_view(), name='draping'),
]
