from django.urls import path, include
from .views import DrapeListView

urlpatterns = [
    path('', DrapeListView.as_view(), name='draping'),
]
