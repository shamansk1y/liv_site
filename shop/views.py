from django.shortcuts import get_object_or_404, render

from cart.cart import Cart
from main_page.context_data import get_page_context
from main_page.views import handle_post_request
from .models import Product


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request,
                  'product_detail.html',
                  {'product': product}
                  )

