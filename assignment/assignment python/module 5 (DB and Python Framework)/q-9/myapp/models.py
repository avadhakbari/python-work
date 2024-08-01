from django.db import models

class ProductMst(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255)

class ProductSubCat(models.Model):
    product_subcat_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(ProductMst, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images')
    product_model = models.CharField(max_length=255)
    product_ram = models.CharField(max_length=255)