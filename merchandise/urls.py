from django.urls import path, include
from .views import MerchandisePageView

urlpatterns = [
    path('merchandise', MerchandisePageView.as_view(), name='merchandise'),
]
