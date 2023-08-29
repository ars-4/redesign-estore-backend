from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from .managers import CustomUserManager


# Create your models here.

class BaseModel(models.Model):
    date_created = models.DateTimeField(default=datetime.datetime.now(), null=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    objects = CustomUserManager()
    def __str__(self):
        return self.email



class Person(BaseModel):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=244, blank=True, null=True)
    last_name = models.CharField(max_length=244, blank=True, null=True)
    email = models.EmailField(null=True)
    street = models.CharField(max_length=244, blank=True, null=True)
    city = models.CharField(max_length=244, blank=True, null=True)
    country = models.CharField(max_length=244, blank=True, default='Pakistan')
    role = models.CharField(max_length=244, blank=True, choices=(
        ('customer', 'customer'),
        ('member', 'member')
    ), default='customer')
    coins = models.CharField(max_length=244, blank=True, default='0')

    def __str__(self):
        return self.first_name



class Images(BaseModel):
    title = models.CharField(max_length=244, blank=True, null=True)
    image = models.ImageField(null=True, upload_to='products/')

    def __str__(self):
        return self.title
    


class ListField(BaseModel):
    title = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.title
    


class Category(BaseModel):
    title = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.title
    


class Badge(BaseModel):
    title = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.title



class Product(BaseModel):
    title = models.CharField(max_length=244, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    bundle = models.ManyToManyField(ListField)
    images = models.ManyToManyField(Images)
    old_price = models.CharField(max_length=244, blank=True, null=True)
    price = models.CharField(max_length=244, blank=True, null=True)
    shipping_price = models.CharField(max_length=244, blank=True, null=True)
    commision = models.CharField(max_length=244, blank=True, null=True)
    total_price = models.CharField(max_length=244, blank=True, null=True)
    employee = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category)
    Badge = models.ForeignKey(Badge, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title



class FrequentlyAskedQuestions(BaseModel):
    question = models.CharField(max_length=244, blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    model = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
    


class CartProduct(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    price = models.CharField(max_length=244, blank=True, null=True)
    quantity = models.CharField(max_length=244, blank=True, null=True)

    def __str__(self):
        return self.product.title

    

class Cart(BaseModel):
    customer = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    cart_products = models.ManyToManyField(CartProduct)
    total_price = models.CharField(max_length=244, null=True, default='0')

    def __str__(self):
        return self.customer.first_name
    


class Order(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    delivery_status = models.CharField(max_length=244, blank=True, choices=(
        ('pending', 'pending'),
        ('shipped', 'shipped'),
        ('delivered', 'delivered'),
        ('declined', 'declined'),
        ('canceled', 'canceled'),
        ('returned', 'returned')
        ), null=True)
    payment_type = models.CharField(max_length=244, blank=True, choices=(
        ('card', 'card'),
        ('payoneer', 'patoneer'),
        ('ethereum', 'ethereum')
    ), null=True)

    def __str__(self):
        return self.delivery_status


