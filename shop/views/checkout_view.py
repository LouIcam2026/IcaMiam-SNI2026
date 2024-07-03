from django.shortcuts import render, redirect
from shop.models import Cart, Order, OrderItem
from shop.forms import CheckoutForm
from shop.services.cart_service import CartService

def index(request):
    
    cart = CartService.get_cart_details(request)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order.objects.create(
                user=request.user,
                nom=form.cleaned_data['nom'],
                prenom=form.cleaned_data['prenom'],
                classe=form.cleaned_data['classe'],
                email=form.cleaned_data['email'],
                time_slot=form.cleaned_data['time_slot'],
            )
            for item in cart.cartitem_set.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
            cart.cartitem_set.all().delete()
            return redirect('shop:order_success')
    else:
        form = CheckoutForm()

    context = {
        'cart': cart,
        'form': form,
    }
    return render(request, 'shop/checkout.html', context)

def order_success(request):
    return render(request, 'shop/order_success.html')
