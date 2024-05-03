from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from django.contrib.auth.models import User 
from django.conf import settings


def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

# Create your models here.


class Category(models.Model):
    cat_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="cat-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    

    def __str__(self):
        return self.title
    
class Tags(models.Model):
    pass


class Vendor(models.Model):
    ven_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="ven-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path)
    discription = models.TextField(null=True,blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True,length=10, max_length=20,prefix="prod-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    Product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=user_directory_path, default="product.jpg")
    discription = models.TextField(null=True,blank=True, default="This is a Product")

    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="99")

    specification = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Products"

    def Product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    

    def __str__(self):
        return self.Product_name


class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images",default="product.jpg")
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Product Images"



class CartOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="99")


    class Meta:
        verbose_name_plural = "Cart Orders"

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999999999999, decimal_places=2, default="99")

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image.url))
    



class Events(models.Model):
    eve_id = ShortUUIDField(unique=True,length=10, max_length=20,prefix="eve-",alphabet="abcdefghijklmnopqrstuvwxyz1234567890")
    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    budget = models.DecimalField(max_digits=999999999999, decimal_places=2, default="99",null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Events"


# class Cart(models.Model):
#     Product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
