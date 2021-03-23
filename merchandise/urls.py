from django.urls import path, include
from .views import MerchandisePageView, LogInPageView, SignUpPageView

urlpatterns = [
    path('accounts', include('allauth.urls')),
    path('merchandise/', MerchandisePageView.as_view(), name='merchandise'),
    path('login/', LogInPageView.as_view(), name='login'),
    path('signup/', SignUpPageView.as_view(), name='signup'),
]
