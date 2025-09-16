from django.db import models
from django.urls import reverse #строит URL по его имени из urls.py


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, unique=True) #db_index - индекс для БД для ускоренного поиска
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name'] #сортирока по полю name
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self): #возвращает ссылку на список товаров в категории
        return reverse('main:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.slug])