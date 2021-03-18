from django.urls import path
from .views import HomePageView, DrapingPageView, LandscapingPageView, MerchandisePageView, ContactPageView

urlpatterns = [
    path('draping/', DrapingPageView.as_view(), name='draping'),
    path('landscaping/', LandscapingPageView.as_view(), name='landscaping'),
    path('merchandise/', MerchandisePageView.as_view(), name='merchandise'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
]
