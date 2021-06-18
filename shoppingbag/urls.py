from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_shoppingbag, name='view_shoppingbag'),
    path('add/<item_id>/', views.add_to_shoppingbag, name='add_to_shoppingbag'),
    path('modify/<item_id>/', views.modify_shoppingbag, name='modify_shoppingbag'),
    path('remove/<item_id>/', views.remove_shoppingbag, name='remove_shoppingbag'),
    path('', views.ShoppingbagPageView.as_view(), name='shoppingbag'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
]

# path('charge/', views.charge, name='charge'),