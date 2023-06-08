from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [
    path('<slug:slug>/', views.product_detail, name='product_detail'),

]