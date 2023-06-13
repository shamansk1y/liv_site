import os
from django.db import models
from django.urls import reverse
from main_page.utils import get_file_name
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils.text import slugify
from PIL import Image



class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Слаг')
    photo = models.ImageField(upload_to=get_file_name, verbose_name='Фото', blank=True, null=True)
    position = models.PositiveIntegerField(default=0, verbose_name='Позиція')
    is_visible = models.BooleanField(default=True, verbose_name='Показувати на сайті')
    category_main_page = models.BooleanField(default=False, verbose_name='Відображення на головній')
    meta_title = models.CharField(max_length=255, verbose_name='Мета-тег Title', blank=True)
    meta_description = models.CharField(max_length=255, verbose_name='Мета-тег Description', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        # проверяем, есть ли изображение
        if self.photo:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.photo)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (255, 255, 255))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.photo.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.photo.save(self.photo.name, ContentFile(img_io.read()), save=False)


        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def get_absolute_url(self):
        return reverse("product_list", args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Слаг')
    article = models.CharField(max_length=200, null=True, blank=True, verbose_name='Артикул')
    image = models.ImageField(upload_to=get_file_name, blank=True, verbose_name='Основне зображення')
    description = models.TextField(blank=True, verbose_name='Опис')
    brand = models.CharField(max_length=200, null=True, blank=True, verbose_name='Бренд')
    weight = models.CharField(max_length=200, null=True, blank=True, verbose_name='Вага')
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name='Країна виробництва')
    application = models.CharField(max_length=200, null=True, blank=True, verbose_name='Застосування')
    warning = models.CharField(max_length=200, null=True, blank=True, verbose_name='Застереження')
    consist = models.CharField(max_length=200, null=True, blank=True, verbose_name='Склад')
    GENDER_CHOICES = [
        ('Ч', 'Чоловіча'),
        ('Ж', 'Жіноча'),
        ('У', 'Унісекс'),
        ]
    characteristics_gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, default='У', verbose_name='Стать')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Категорія')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Ціна зі знижкою')
    position = models.PositiveIntegerField(default=1, verbose_name='Позиція')
    STASTUS_CHOICES = [
        ('Н', 'Немає в наявності'),
        ('В', 'В наявності'),
        ('П', 'Під замовлення 2-3 дні'),
        ('C', 'Скоро в наявності'),
        ]
    status = models.CharField(max_length=1, choices=STASTUS_CHOICES, blank=True, default='Н', verbose_name='Наявність')
    available = models.BooleanField(default=True, verbose_name='Видимисть на сайті')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата редагування')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug])

    def save(self, *args, **kwargs):
        # проверяем, есть ли изображение
        if self.image:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.image)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (245, 245, 245))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.image.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.image.save(self.image.name, ContentFile(img_io.read()), save=False)

        super(Product, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товари'

class RecommendedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ['position']
        verbose_name_plural = 'Рекомендовані товари'

    def __str__(self):
        return self.product.name



class SubProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='subproductimages')
    image = models.ImageField(upload_to=get_file_name, blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product.slug)
        # проверяем, есть ли изображение с таким же slug
        i = 1
        while SubProductImage.objects.filter(product=self.product, slug=self.slug).exists():
            i += 1
            self.slug = f"{slugify(self.product.slug)}-{i}"
        if self.image:
            # открываем изображение с помощью библиотеки PIL
            img = Image.open(self.image)

            # проверяем, является ли изображение квадратным
            if img.width != img.height:
                size = (max(img.width, img.height), max(img.width, img.height))
                img_with_border = Image.new("RGB", size, (245, 245, 245))
                x = (size[0] - img.width) // 2
                y = (size[1] - img.height) // 2
                img_with_border.paste(img, (x, y))

                # получаем формат изображения из имени файла
                file_ext = os.path.splitext(self.image.name)[1].lower()
                format_dict = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.gif': 'GIF'}
                image_format = format_dict.get(file_ext, 'JPEG')

                # сохраняем квадратное изображение в том же формате, что и оригинал
                img_io = BytesIO()
                img_with_border.save(img_io, format=image_format)
                img_io.seek(0)
                self.image.save(self.image.name, ContentFile(img_io.read()), save=False)


        super(SubProductImage, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Дополнительные изображения товара'

    def __str__(self):
        return f'{self.product.name} - {self.id}'