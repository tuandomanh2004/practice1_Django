from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Product , Category , Review
# Create your views here.
class ShowProducts(ListView) : 
    model = Product
    template_name = "show_products.html"
    context_object_name = 'all_products'

# class ProductDetail(DetailView) : 
#     model = Product
#     template_name = "product_detail.html"
#     context_object_name = 'product'
def show_detail(request , pk) : 
    product = Product.objects.get(pk = pk)
    review = Review.objects.filter(product = product) 
    return render(request , 'product_detail.html' , {'product' : product , 'review' : review})    