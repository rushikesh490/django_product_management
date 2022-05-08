    from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return str(self.name)

class Product(models.Model):
    type_choice = [
        ('Men','Men'),
        ('Women','Women'),
        ('Redmi','Redmi'),
        ('Samsung','Samsung'),
        ('iphone','iphone'),
        ('vegetable','vegetable'),
    ]
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)
    type = models.CharField(max_length=10,null=True,blank=True,choices=type_choice)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    discount_price = models.FloatField(default=0.0,null=True)
    description = models.TextField(max_length=500)
    prod_img = models.ImageField(upload_to='products',null=True)

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


class Register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_num = models.IntegerField()

    def __str__(self):
        return str(self.user.username)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    phone_num = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    date = models.DateField(default=datetime.datetime.today)

    def place_order(self):
        self.save()
    def __str__(self):
        return self.user
    
