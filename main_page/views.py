from django.shortcuts import render, redirect, get_object_or_404
from main_page.context_data import get_page_context
from main_page.forms import ContactUsForm, SubscriptionForm


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
    # cart = Cart(request)

    if request.method == 'POST':
        handle_post_request(request)
    data = {
        # 'cart': cart,
    }
    context_req = get_page_context(request)
    # context_data = get_common_context()
    # data.update(context_data)
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