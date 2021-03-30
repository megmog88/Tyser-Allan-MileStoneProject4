from django.urls import path, include
from .views import HomePageView, DrapingPageView, LandscapingPageView
from . import views

urlpatterns = [
    path('draping/', DrapingPageView.as_view(), name='draping'),
    path('landscaping/', LandscapingPageView.as_view(), name='landscaping'),
    path('contact/', views.ContactView, name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
]
