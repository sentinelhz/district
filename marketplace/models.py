from django.db import models
from account.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime

from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
def category_image_path(instance, filename):
    return "category/icons/{}/{}".format(instance.name, filename)


def product_image_path(instance, filename):
    return "product/images/{}/{}".format(instance.title, filename)

class Category(models.Model):
    title = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=100, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.title





STATUS = (
    ('order_accepted', 'Order Accepted'),
    ('outForDelivery', 'Out For Delivery'),
    ('delivered', 'Delivered')
)


DISCOUNT_TYPE = (
    ('flat', 'flat'),
    ('percent', 'percent')
)
# Create your models here.

class Product(models.Model):
    product_tag = models.CharField(max_length=10,null=False,blank=True)
    name = models.CharField(max_length=100,null=False,blank=False)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageUrl = models.ImageField(upload_to=product_image_path, blank=True)
    created_by = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    payment_method = models.CharField(max_length=100, blank=True, null=True)
    taxPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    shippingPrice = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2, default = 0)
    coupon = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, blank=True, null=True)
    isPaid = models.BooleanField(default=False)
    isDelivered = models.BooleanField(default=False)
    transactionId = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self._id)

    class Meta:
        ordering = ['-created_at']

class Cart(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True)



    def __str__(self):
        return str(self.order._id)


class ShippingAddress(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=400, blank=True, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.order._id)



class Coupons(models.Model):
    code = models.CharField(max_length=20)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    max_limit = models.IntegerField(default=1)

    def __str__(self):
        return self.is_active


class Testimonials(models.Model):
    STATUS = ((0,"Draft"),(1,"Publish"))
    status = models.CharField(max_length=20, choices=STATUS)
    title = models.TextField(max_length=1250, unique=False)
    customer_name = models.CharField(max_length=200, null=True)
    #slug = models.SlugField(max_length=200, unique=False)
    updated_on = models.DateTimeField(auto_now= True)



    def __str__(self):
        return self.title
