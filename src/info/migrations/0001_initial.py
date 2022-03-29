# Generated by Django 3.1 on 2022-03-28 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренд',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=100)),
                ('created', models.DateTimeField()),
                ('title', models.CharField(max_length=255)),
                ('manufacturer_url', models.CharField(blank=True, max_length=500, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('lenght', models.IntegerField(blank=True, null=True)),
                ('hight', models.IntegerField(blank=True, null=True)),
                ('depth', models.IntegerField(blank=True, null=True)),
                ('description_short', models.TextField(blank=True, null=True)),
                ('description_main', models.TextField(blank=True, null=True)),
                ('description_specs', models.TextField(blank=True, null=True)),
                ('description_package', models.TextField(blank=True, null=True)),
                ('description_features', models.TextField(blank=True, null=True)),
                ('description_simplified', models.TextField(blank=True, null=True)),
                ('time_update', models.DateTimeField(blank=True, null=True)),
                ('bp1', models.CharField(blank=True, max_length=255, null=True)),
                ('bp2', models.CharField(blank=True, max_length=255, null=True)),
                ('bp3', models.CharField(blank=True, max_length=255, null=True)),
                ('bp4', models.CharField(blank=True, max_length=255, null=True)),
                ('bp5', models.CharField(blank=True, max_length=255, null=True)),
                ('bp6', models.CharField(blank=True, max_length=255, null=True)),
                ('bp7', models.CharField(blank=True, max_length=255, null=True)),
                ('bp8', models.CharField(blank=True, max_length=255, null=True)),
                ('bp9', models.CharField(blank=True, max_length=255, null=True)),
                ('bp10', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='info.brand')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'unique_together': {('sku', 'brand')},
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.CharField(blank=True, max_length=100, null=True)),
                ('is_main', models.BooleanField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='info.product')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]