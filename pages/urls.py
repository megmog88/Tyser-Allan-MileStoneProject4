from django.urls import path, include
from .views import HomePageView, DrapingPageView, LandscapingPageView, ContactPageView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('draping/', DrapingPageView.as_view(), name='draping'),
    path('landscaping/', LandscapingPageView.as_view(), name='landscaping'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
