from django.db import models
from main_page.utils import get_file_name, get_file_name_id
from django.utils import timezone

class Slider(models.Model):

    title = models.CharField(max_length=50, verbose_name="Назва слайду")
    position = models.SmallIntegerField(verbose_name="Позиція")
    image = models.ImageField(upload_to=get_file_name_id, verbose_name="Зображення")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    h_1 = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=500, blank=True, verbose_name="Опис")
    tab = models.CharField(max_length=50, blank=True, verbose_name="Текст кнопки")
    tab_url = models.URLField(blank=True, verbose_name="Посилання з кнопки")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)
        verbose_name_plural = 'Слайдер'


class ContactUs(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=250, blank=True)
    subject = models.CharField(max_length=50)

    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Зворотній зв'язок"



class Contacts(models.Model):

    address = models.CharField(max_length=70, verbose_name="Адреса")
    phone = models.CharField(blank=True, max_length=50, verbose_name="Телефон 1")
    email = models.CharField(max_length=50, verbose_name="Пошта ")
    fb_url = models.URLField(blank=True, verbose_name="Посилання на facebook", default='https://www.facebook.com/')
    youtube_url = models.URLField(blank=True, verbose_name="Посилання на youtube", default='https://www.youtube.com/')
    in_url = models.URLField(blank=True, verbose_name="Посилання на instagram", default='https://www.instagram.com/')

    def __str__(self):
        return f'{self.address}'

    class Meta:
        ordering = ('address',)
        verbose_name_plural = 'Контакти'


class Subscription(models.Model):

    email = models.EmailField()
    date = models.DateField(auto_now_add=True )
    date_processing = models.DateField(auto_now=True )
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.date}: {self.email}'

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = 'Підписка на email розсилку'



class About(models.Model):
    title = models.CharField(max_length=250, blank=True, verbose_name="Заголовок")
    desc = models.TextField(max_length=1000, verbose_name="Опис")
    is_visible = models.BooleanField(default=True, verbose_name="Видимість")
    image = models.ImageField(upload_to=get_file_name_id, verbose_name="Зображення")
    tab_name = models.CharField(max_length=70, verbose_name="Текст кнопки", default='Скачати актуальний каталог')
    cat_url = models.URLField(blank=True, verbose_name="Посилання на актуальний каталог",
                             default='"https://drive.google.com/file/d/1Hcbe8G_xCCVQkd-r-uhrJQ95EX2FsaFl/view')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Про нас'