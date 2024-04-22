from django.urls import path
from .views import hello_view, fun_view, main_view, product_list, product_detail, home_view, create_product

urlpatterns = [
    path('hello/', hello_view, name='hello'),
    path('fun/', fun_view, name='fun'),
    path('main/', main_view, name='main'),
    path('products/', product_list, name='product_list'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('', home_view, name='home'),
    path('create/', create_product, name='create_product'),

]
