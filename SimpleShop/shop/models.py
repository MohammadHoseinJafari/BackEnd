from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.forms import ModelForm
from django.db.models import Avg
from django.db.models.signals import post_save

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200,verbose_name='نام کالا')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:category', args=[self.slug, self.id])

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    unit_price = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    color = models.ManyToManyField('Color',blank=True)
    size = models.ManyToManyField('Size',blank=True)
    image = models.ImageField(upload_to='img', height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'

class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'اندازه'
        verbose_name_plural = 'اندازه ها'

class Client(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    zipcode = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

class Stuff(models.Model):
    stuff_name=models.CharField(max_length=200)
    phone = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.stuff_name

    class Meta:
        verbose_name = 'پرسنل'
        verbose_name_plural = 'پرسنل'

class Supplier(models.Model):
    Supp_name=models.CharField(max_length=200)
    Supp_phone = models.BigIntegerField(null=True, blank=True)
    Supp_address = models.CharField(max_length=250)

    def __str__(self):
        return self.Supp_name

    class Meta:
        verbose_name = 'تامین کننده'
        verbose_name_plural = 'تامین کنندگان'


class Post(models.Model):
    name=models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    disc = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پست ها'
        verbose_name_plural = 'پست'
