from django.db import models


# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='/static/shop/images/')
    price = models.CharField(max_length=10)
    discount = models.CharField(max_length=10, blank=True, null=True)
    price_sale = models.CharField(max_length=10, blank=True, null=True)



    def __str__(self):
        return f'{self.id} - {self.name}'

