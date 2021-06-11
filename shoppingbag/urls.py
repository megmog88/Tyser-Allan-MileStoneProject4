from django.urls import path
from . import views
from shoppingbag.views import (
    SuccessView,
    CancelView,
)

urlpatterns = [
    path('', views.view_shoppingbag, name='view_shoppingbag'),
    path('add/<item_id>/', views.add_to_shoppingbag, name='add_to_shoppingbag'),
    path('modify/<item_id>/', views.modify_shoppingbag, name='modify_shoppingbag'),
    path('remove/<item_id>/', views.remove_shoppingbag, name='remove_shoppingbag'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('stripe/create-checkout-session', views.create_checkout_session, name="stripe_create_checkout_session"),
  


]
