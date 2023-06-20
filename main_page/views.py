from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from cart.cart import Cart
from main_page.context_data import get_page_context, get_common_context
from main_page.forms import ContactUsForm, SubscriptionForm
from shop.models import Product, Category
from django.db.models import Q

def handle_post_request(request):

    contact_us = ContactUsForm(request.POST)
    subscription = SubscriptionForm(request.POST)

    if contact_us.is_valid():
        contact_us.save()
        return redirect('/')
    if subscription.is_valid():
        subscription.save()
        return redirect('/')


def index(request):
    cart = Cart(request)

    if request.method == 'POST':
        handle_post_request(request)
    data = {
        'cart': cart,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'index.html', context=data)


def contacts(request):
    if request.method == 'POST':
        handle_post_request(request)
    data = get_page_context(request)
    return render(request, 'contact.html', context=data)


def about(request):
    if request.method == 'POST':
        handle_post_request(request)

    data = get_page_context(request)
    return render(request, 'about.html', context=data)


def product_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, available=True)
    cart = Cart(request)
    sort = request.GET.get('sort', '')  # get sorting parameter

    # sort products
    if sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'date_desc':
        products = products.order_by('-created')
    else:
        products = products.order_by('position')

    # paginator
    count = 2  # количество товаров по умолчанию на странице
    count_param = request.GET.get('count')
    if count_param and count_param.isdigit():
        count = int(count_param)
    paginator = Paginator(products, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj': page_obj,
        'cart': cart,
        'products': page_obj,
        'category': category,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'list.html', context=data)


def search(request):
    query = request.GET.get('q')
    search_products = Product.objects.filter(Q(name__icontains = query) | Q(description__icontains=query))
    data = {
        'search_products': search_products,
        'query': query,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'search.html', context=data)