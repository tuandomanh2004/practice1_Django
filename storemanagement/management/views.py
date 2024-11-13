from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , DeleteView , UpdateView
from django.urls import reverse_lazy
from .models import Product , Category , Review
# Create your views here.
def home(request) : 
    return render(request , 'base.html')
def show_detail(request , pk) : 
    product = Product.objects.get(pk = pk)
    review = Review.objects.filter(product = product) 
    return render(request , 'product_detail.html' , {'product' : product , 'review' : review})  
class ShowProducts(ListView) : 
    model = Product
    template_name = "show_products.html"
    context_object_name = 'all_products'  
class ProductCreateView(CreateView) : 
    model = Product
    template_name = 'new_product.html'
    fields = '__all__'
class ProductUpdateView(UpdateView) :
    model = Product
    template_name = 'update_product.html'
    fields = '__all__'
class ProductDeleteView(DeleteView) :
    model = Product
    template_name = 'delete_product.html'
    success_url = reverse_lazy('home')
