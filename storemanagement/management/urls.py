from django.urls import path
from .views import ShowProducts , show_detail 
urlpatterns = [
    path('' , ShowProducts.as_view() , name = 'show_prducts' ),
    path('product/<int:pk>' , show_detail , name = 'product_detail')
]