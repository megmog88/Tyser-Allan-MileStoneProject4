from django.urls import path, include
from .views import HomePageView
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    path('success/', views.contact, name='success'),
]
