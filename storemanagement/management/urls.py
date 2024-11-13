from django.urls import path
from .views import ShowProducts,ProductCreateView,ProductUpdateView,home,show_detail 
urlpatterns = [
    path('' , home , name = 'home' ),
    path('product/showproducts/' , ShowProducts.as_view() , name = 'show_products'),
    path('product/new/' , ProductCreateView.as_view() , name = 'product_new'),
    path('product/<int:pk>' , show_detail , name = 'product_detail'),
    path('product/<int:pk>/edit' , ProductUpdateView.as_view() , name = 'product_edit' )
]