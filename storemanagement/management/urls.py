from django.urls import path
from .views import ShowProducts , show_detail ,ProductCreateView,home
urlpatterns = [
    path('' , home , name = 'home' ),
    path('product/showproducts/' , ShowProducts.as_view() , name = 'show_products'),
    path('product/<int:pk>' , show_detail , name = 'product_detail'),
    path('product/new/' , ProductCreateView.as_view() , name = 'product_new')
]