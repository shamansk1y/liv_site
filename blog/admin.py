from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    model = Blog
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'is_visible', 'pub_date')
    list_editable = ['slug', 'is_visible']
    list_filter = ('is_visible', 'pub_date')
    search_fields = ('title',)

