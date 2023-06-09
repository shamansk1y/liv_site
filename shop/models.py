from django.db import models
from django.urls import reverse
from main_page.utils import get_file_name


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва')
    slug = models.SlugField(unique=True, blank=True, null=True, verbose_name='Слаг')
    meta_title = models.CharField(max_length=255, verbose_name='Мета-тег Title', blank=True)
    meta_description = models.CharField(max_length=255, verbose_name='Мета-тег Description', blank=True)
    position = models.PositiveIntegerField(default=0, verbose_name='Позиція')
    is_visible = models.BooleanField(default=True, verbose_name='Показувати на сайті')

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


    def get_absolute_url(self):
        return reverse("product_list", args=[self.slug])

    def __str__(self):
        return self.name


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

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товари'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug])
