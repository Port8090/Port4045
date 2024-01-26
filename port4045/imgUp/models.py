from django.db import models

# Create your models here.
""" class Product(models.Model):
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
        verbose_name_plural = '제품' """

""" class Product(models.Model) :
    colPath = models.FileField(upload_to='Uploaded Files/%y/%m/%d/', blank=True)
    colDay = models.DateField(auto_now = True) """

class imgeupload(models.Model):
    title = models.CharField(max_length=30, null=True)
    image = models.ImageField(upload_to='about_me/awards/&Y/%m/%d', blank=True)

    create_at = models.DateTimeField(null=True, blank=True)
    update_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'