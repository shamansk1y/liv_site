from django.shortcuts import get_object_or_404, render

from cart.cart import Cart
from main_page.context_data import get_page_context, get_common_context
from main_page.views import handle_post_request
from .models import Product



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    if request.method == 'POST':
        handle_post_request(request)
    data = {
        'product': product,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'product_detail.html', context=data)

