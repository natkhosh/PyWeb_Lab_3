from django.db import models
from vshop import settings

# Create your models here.

if settings.LANG == 'ru':
    lang_ru= settings.LANG

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50, null=True)
    image = models.ImageField(upload_to='uploads')
    price = models.CharField(max_length=10)
    discount = models.CharField(max_length=10, blank=True, null=True)
    price_sale = models.CharField(max_length=10, blank=True, null=True)



    def __str__(self):
        return f'{self.id} - {self.name}'

