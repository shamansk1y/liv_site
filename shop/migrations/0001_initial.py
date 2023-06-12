# Generated by Django 4.2.1 on 2023-06-12 08:35

from django.db import migrations, models
import django.db.models.deletion
import main_page.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='Слаг')),
                ('meta_title', models.CharField(blank=True, max_length=255, verbose_name='Мета-тег Title')),
                ('meta_description', models.CharField(blank=True, max_length=255, verbose_name='Мета-тег Description')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Позиція')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Показувати на сайті')),
            ],
            options={
                'verbose_name': 'Категорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=200, verbose_name='Слаг')),
                ('article', models.CharField(blank=True, max_length=200, null=True, verbose_name='Артикул')),
                ('image', models.ImageField(blank=True, upload_to=main_page.utils.get_file_name, verbose_name='Основне зображення')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('brand', models.CharField(blank=True, max_length=200, null=True, verbose_name='Бренд')),
                ('weight', models.CharField(blank=True, max_length=200, null=True, verbose_name='Вага')),
                ('country', models.CharField(blank=True, max_length=200, null=True, verbose_name='Країна виробництва')),
                ('application', models.CharField(blank=True, max_length=200, null=True, verbose_name='Застосування')),
                ('warning', models.CharField(blank=True, max_length=200, null=True, verbose_name='Застереження')),
                ('consist', models.CharField(blank=True, max_length=200, null=True, verbose_name='Склад')),
                ('characteristics_gender', models.CharField(blank=True, choices=[('Ч', 'Чоловіча'), ('Ж', 'Жіноча'), ('У', 'Унісекс')], default='У', max_length=1, verbose_name='Стать')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('discounted_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Ціна зі знижкою')),
                ('position', models.PositiveIntegerField(default=1, verbose_name='Позиція')),
                ('status', models.CharField(blank=True, choices=[('Н', 'Немає в наявності'), ('В', 'В наявності'), ('П', 'Під замовлення 2-3 дні'), ('C', 'Скоро в наявності')], default='Н', max_length=1, verbose_name='Наявність')),
                ('available', models.BooleanField(default=True, verbose_name='Видимисть на сайті')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата редагування')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name_plural': 'Товари',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
