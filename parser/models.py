from django.db import models
 
class CatalogBrand(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_brand'


class CatalogImage(models.Model):
    image_file = models.CharField(max_length=100, blank=True, null=True)
    is_main = models.BooleanField(blank=True, null=True)
    product_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_image'


class CatalogProduct(models.Model):
    sku = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    manufacturer_url = models.TextField(blank=True, null=True)  # This field type is a guess.
    weight = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    lenght = models.IntegerField(blank=True, null=True)
    hight = models.IntegerField(blank=True, null=True)
    depth = models.IntegerField(blank=True, null=True)
    description_short = models.TextField(blank=True, null=True)
    description_main = models.TextField(blank=True, null=True)
    description_specs = models.TextField(blank=True, null=True)
    description_package = models.TextField(blank=True, null=True)
    description_features = models.TextField(blank=True, null=True)
    description_simplified = models.TextField(blank=True, null=True)
    time_update = models.DateTimeField(blank=True, null=True)
    bp1 = models.TextField(blank=True, null=True)
    bp2 = models.TextField(blank=True, null=True)
    bp3 = models.TextField(blank=True, null=True)
    bp4 = models.TextField(blank=True, null=True)
    bp5 = models.TextField(blank=True, null=True)
    bp6 = models.TextField(blank=True, null=True)
    bp7 = models.TextField(blank=True, null=True)
    bp8 = models.TextField(blank=True, null=True)
    bp9 = models.TextField(blank=True, null=True)
    bp10 = models.TextField(blank=True, null=True)
    brand = models.ForeignKey(CatalogBrand, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalog_product'
        verbose_name = 'Новый Продукт'
        verbose_name_plural = 'Новые Продукты'

    def __str__(self):
        return self.sku