from django.db import models
from datetime import timezone
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    isim = models.CharField(max_length=101)
    genel = models.CharField(max_length = 51)
    aciklama = models.CharField(max_length = 200)   
    fiyat = models.IntegerField(default = 1)
    marka = models.CharField(max_length=51)
    tur = models.CharField(max_length = 50)
    image = models.FilePathField(path="/img")

    class Meta:
        db_table = 'products'

class Comment(models.Model):
    isim = models.CharField(max_length=100)
    baslik = models.CharField(max_length = 50)
    yorum = models.CharField(max_length = 200)   
    puan = models.IntegerField(default = 1)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='comments')

    class Meta:
        db_table = 'comments'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    class Meta:
        db_table = 'orders'
