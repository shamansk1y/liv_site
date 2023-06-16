from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from cart.cart import Cart
from main_page.context_data import get_page_context, get_common_context
from main_page.forms import ReviewForm
from main_page.models import Review
from main_page.views import handle_post_request
from .models import Product



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    average_rating = Review.objects.aggregate(Avg('rating'))['rating__avg']
    review_app = product.review_set.filter(is_approved=True)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.save()
            form = ReviewForm()
    else:
        form = ReviewForm()
    data = {
        'average_rating': average_rating,
        'review_app': review_app,
        'product': product,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    data['form'] = form
    return render(request, 'product_detail.html', context=data)


