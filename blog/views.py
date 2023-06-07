from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blog
from main_page.context_data import get_common_context, get_page_context


def blog_post_list(request):

    posts = Blog.objects.filter(is_visible=True).order_by('-pub_date')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {
        'posts': posts,
        'page_obj': page_obj,
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'post_list.html', context=data)

def blog_post_detail(request, slug):

    post = get_object_or_404(Blog, slug=slug, is_visible=True)
    data = {
        'post': post
    }
    context_req = get_page_context(request)
    context_data = get_common_context()
    data.update(context_data)
    data.update(context_req)
    return render(request, 'post_detail.html', context=data)
