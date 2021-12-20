from django.db import models

class WyrestormItem(models.Model):
    article = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description_min = models.TextField(blank=True, null=True)
    description_max = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    image_count = models.IntegerField(blank=True, null=True)
    image_links = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wyrestorm_items'

    def __str__(self):
        return self.name


class WyrestormItemsUpdate(models.Model):
    article = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description_min = models.TextField(blank=True, null=True)
    description_max = models.TextField(blank=True, null=True)
    features = models.TextField(blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    image_count = models.IntegerField(blank=True, null=True)
    image_links = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'wyrestorm_items_update'

    def __str__(self):
        return self.name