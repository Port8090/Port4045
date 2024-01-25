from django.db import models

# Create your models here.
class Product(models.Model):
    product = models.CharField(max_length=32,verbose_name='product_name')
    price = models.IntegerField(verbose_name='product_price')
    description = models.TextField(verbose_name='product_description')
    image = models.ImageField(blank=True, null=True, verbose_name='product_image')
    stock = models.IntegerField(verbose_name='product_stock')
    register_date = models.DateTimeField(auto_now_add=True, verbose_name='product_register_date')

    def __str__(self):
        return self.product

    class Meta:
        db_table = 'product_table'
        verbose_name = '제품'
        verbose_name_plural = '제품'