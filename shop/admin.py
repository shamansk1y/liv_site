from django.contrib import admin
from .models import Product, Category, RecommendedProduct, SubProductImage


class SubProductImageInline(admin.TabularInline):
    model = SubProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'discounted_price', 'price', 'category', 'available']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'discounted_price', 'available', 'category']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [SubProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','position', 'is_visible']
    list_editable = ['position', 'is_visible']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(RecommendedProduct)
class RecommendedProduct(admin.ModelAdmin):
    model = RecommendedProduct
    list_filter = ['position']