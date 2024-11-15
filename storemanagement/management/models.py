from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model) : 
    name = models.CharField(max_length=100)
    def __str__(self) : 
        return self.name

class Product(models.Model) :
    name = models.CharField(max_length =200)
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    price = models.IntegerField(default= 0)
    quantity = models.IntegerField(default= 0)
    def __str__(self) : 
        return self.name
    def get_absolute_url(self) : 
        return reverse('product_detail' , args = [str(self.id)])
    
class Review(models.Model) : 
    title = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User',on_delete= models.CASCADE)
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    content = models.TextField()
    def __str__(self) : 
        return self.title