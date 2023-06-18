from django.urls import path
from .views import upload_csv_view, product_detail

app_name = 'shop'

urlpatterns = [
    path('<slug:slug>/', product_detail, name='product_detail'),


]