from django.urls import path
from .views import LandscapingListView, LandscapingDetailView

urlpatterns = [
    path('landscaping', LandscapingListView.as_view(), name='landscaping'),
    path('object/<int:pk>/', LandscapingDetailView.as_view(), name='landscapinginfo'),
]
