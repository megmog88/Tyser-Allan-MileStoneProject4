from django.urls import path, include
from .views import HomePageView
from . import views

urlpatterns = [
    path('contact/', views.ContactView, name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
]
