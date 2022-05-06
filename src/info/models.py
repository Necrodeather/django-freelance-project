from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        app_label = 'info'
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренд'

    def __str__(self):
        return self.name


class Image(models.Model):
    image_file = models.CharField(max_length=100, blank=True, null=True)
    is_main = models.BooleanField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        app_label = 'info'
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    

class Product(models.Model):
    sku = models.CharField(max_length=100)
    created = models.DateTimeField()
    title = models.CharField(max_length=255)
    manufacturer_url = models.CharField(max_length=500, blank=True, null=True)
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
    bp1 = models.CharField(max_length=255, blank=True, null=True)
    bp2 = models.CharField(max_length=255, blank=True, null=True)
    bp3 = models.CharField(max_length=255, blank=True, null=True)
    bp4 = models.CharField(max_length=255, blank=True, null=True)
    bp5 = models.CharField(max_length=255, blank=True, null=True)
    bp6 = models.CharField(max_length=255, blank=True, null=True)
    bp7 = models.CharField(max_length=255, blank=True, null=True)
    bp8 = models.CharField(max_length=255, blank=True, null=True)
    bp9 = models.CharField(max_length=255, blank=True, null=True)
    bp10 = models.CharField(max_length=255, blank=True, null=True)
    brand = models.ForeignKey(Brand, models.DO_NOTHING)
    unique = models.BooleanField(blank=True, default=False)

    class Meta:
        app_label = 'info'
        unique_together = (('sku', 'brand'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def __str__(self):
        return self.sku