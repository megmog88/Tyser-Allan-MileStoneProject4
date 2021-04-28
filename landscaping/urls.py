from django.urls import path
from .views import LandscapingListView, LandscapingDetailView

urlpatterns = [
    path('landscaping', LandscapingListView.as_view(), name='landscaping'),
    path('landscapes/<int:pk>/', LandscapingDetailView.as_view(), name='landscapinginfo'),
]
