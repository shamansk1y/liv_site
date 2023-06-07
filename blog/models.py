from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

from main_page.utils import get_file_name_id
from shop.models import Product

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    is_visible = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_file_name_id)
    position = models.IntegerField(default=0)
    content = RichTextField()
    meta_title = models.CharField(max_length=255, null=True, blank=True)
    meta_description = models.CharField(max_length=255, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    blog_products = models.ManyToManyField(Product, blank=True)

    class Meta:
        ordering = ('-pub_date',)
        verbose_name_plural = 'Блог'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_post_detail', kwargs={'slug': self.slug})
