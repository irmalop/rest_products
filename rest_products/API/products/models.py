from tabnanny import verbose
from unicodedata import category
from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status_delete = models.BooleanField(default=False)

    class Meta:
            verbose_name = 'Category'
            verbose_name_plural = 'Categories'
            db_table = 'Category'
            ordering = ['id']

class Provider(models.Model):

    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.CharField(max_length=10)
    rfc = models.CharField(max_length=13)
    status_delete = models.BooleanField(default=False)
    
    class Meta:
            verbose_name = 'Provider'
            verbose_name_plural = 'Providers'
            db_table = 'provider'
            ordering = ['id']

class Product(models.Model):

    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.CharField(max_length=100)
    price_s = models.FloatField(blank=True)
    price_c = models.FloatField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, blank=False)
    status_delete = models.BooleanField(default=False)
   
    class Meta:
            verbose_name = 'Product'
            verbose_name_plural = 'Products'
            db_table = 'product'
            ordering = ['id']