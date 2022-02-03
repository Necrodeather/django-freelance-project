# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    source_name = models.TextField(blank=True, null=True)
    image_count = models.IntegerField(blank=True, null=True)
    image_links = models.TextField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'catalog_product'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
