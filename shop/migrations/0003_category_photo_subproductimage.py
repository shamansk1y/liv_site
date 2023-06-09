# Generated by Django 4.2.1 on 2023-06-13 08:02

from django.db import migrations, models
import django.db.models.deletion
import main_page.utils


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_recommendedproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=main_page.utils.get_file_name, verbose_name='Фото'),
        ),
        migrations.CreateModel(
            name='SubProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=main_page.utils.get_file_name)),
                ('slug', models.SlugField(blank=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subproductimages', to='shop.product')),
            ],
            options={
                'verbose_name_plural': 'Дополнительные изображения товара',
            },
        ),
    ]
