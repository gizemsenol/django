
from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100, verbose_name='ürün ismi')
    content = models.TextField(verbose_name='ürün açıklaması', max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(verbose_name='Aktif', default=True)
    stock_count = models.PositiveSmallIntegerField(verbose_name='stok_adedi')
    price = models.DecimalField(verbose_name='ürün fiyatı', decimal_places=2, max_digits=10)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        db_table = 'urunler'