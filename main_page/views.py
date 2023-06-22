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
    sort = request.GET.get('sort', '')  # получаем параметр сортировки

    # Сортируем товары
    if sort == 'price_desc':
        products = products.order_by('-price')
    elif sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'date_desc':
        products = products.order_by('-created')
    else:
        products = products.order_by('position')

    # Получаем параметры фильтрации по цене
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Фильтруем товары по диапазону цен
    if min_price and max_price:
        products = products.filter(discounted_price__range=(min_price, max_price))

    # Пагинация
    count = 18  # количество товаров по умолчанию на странице
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
        'min_price': min_price,
        'max_price': max_price,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'list.html', context=data)



def search(request):
    query = request.GET.get('q')
    search_products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Pagination
    count = 16  # количество товаров по умолчанию на странице
    count_param = request.GET.get('count')
    if count_param and count_param.isdigit():
        count = int(count_param)
    paginator = Paginator(search_products, count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'search_products': page_obj,
        'query': query,
        'page_obj': page_obj,
    }

    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)

    return render(request, 'search.html', context=data)