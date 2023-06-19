from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from cart.cart import Cart
from main_page.context_data import get_page_context, get_common_context
from main_page.forms import ReviewForm
from main_page.models import Review
from main_page.views import handle_post_request
from .models import Product
from django.contrib import messages
from django.core.files.base import ContentFile
import csv
import requests
from django.utils.text import slugify

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


def upload_csv_view(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('csv_file')
        if csv_file.name.endswith('.csv'):
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            for row in reader:
                name = row['name']
                slug = slugify(name)  # Создание слага из названия

                # Остальные поля из CSV файла

                # Загрузка изображения
                image_url = row['image']
                response = requests.get(image_url)
                if response.status_code == 200:
                    image_name = image_url.split('/')[-1]
                    image_content = response.content
                    product = Product(name=name, slug=slug)
                    product.image.save(image_name, ContentFile(image_content), save=False)
                else:
                    messages.warning(request, f"Не удалось загрузить изображение для товара '{name}'")

                # Создание и сохранение товара
                product = Product(name=name, slug=slug)
                product.article = row['article']
                product.description = row['description']
                product.brand = row['brand']
                product.weight = row['weight']
                product.country = row['country']
                product.application = row['application']
                product.warning = row['warning']
                product.consist = row['consist']
                product.price = row['price_old']
                product.discounted_price = row['price_new']
                # Заполните остальные поля товара

                product.save()

            messages.success(request, 'CSV файл успешно загружен и товары добавлены')
        else:
            messages.error(request, 'Пожалуйста, выберите файл с расширением .csv')
    return render(request, 'upload_form.html')
