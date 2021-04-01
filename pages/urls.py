from django.urls import path, include
from .views import HomePageView, LandscapingPageView
from . import views

urlpatterns = [
    path('landscaping/', LandscapingPageView.as_view(), name='landscaping'),
    path('contact/', views.ContactView, name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
]
