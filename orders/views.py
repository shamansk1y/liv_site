from django.shortcuts import render
from cart.cart import Cart
from main_page.context_data import get_page_context, get_common_context
from main_page.views import handle_post_request
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                order_item = OrderItem(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
                order_item.save()
                order_item.order_number = str(100000 + order_item.order_id)
                order_item.save()

            # clear the cart
            cart.clear()
            if request.method == 'POST':
                handle_post_request(request)
            data = {
                'order': order
            }
            context_req = get_page_context(request)
            context_data = get_common_context()
            data.update(context_data)
            data.update(context_req)
            return render(request, 'created.html', context=data)
    else:
        form = OrderCreateForm()

    data = {
        'cart': cart,
        'form': form
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'create.html', context=data)


