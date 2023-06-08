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
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    article = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=get_file_name, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    position = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Товари'
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.slug])
