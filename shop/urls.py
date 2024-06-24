from django.urls import path, include
from shop.views import shop_view
from shop.views import cart_view
from shop.views import checkout_view

app_name="shop"


urlpatterns = [
    # shop
    path('', shop_view.index, name='home'),
    path('page/<str:slug>', shop_view.display_page, name='page'),
    path('product/<str:slug>', shop_view.display_product, name='single_product'),
    path('shop', shop_view.shop, name='shop_list'),

    # cart
    path('cart', cart_view.index, name='cart'),
    path('cart/add/<int:product_id>', cart_view.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/<int:quantity>', cart_view.remove_from_cart, name='remove_from_cart'),

    #checkout
    path('checkout', checkout_view.index, name='checkout'),
]
