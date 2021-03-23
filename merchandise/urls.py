from django.urls import path, include
from .views import MerchandisePageView

urlpatterns = [
    path('accounts', include('allauth.urls')),
    path('merchandise', MerchandisePageView.as_view(), name='merchandise'),
]
