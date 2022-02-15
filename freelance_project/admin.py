from django.contrib import admin
from django.apps import apps
from .models import CatalogProduct as main
from parser.models import CatalogProduct as parser

#Название админ панели
admin.site.site_header = 'Admin-panel'

admin.site.register(main)





class MultiDBModelAdmin(admin.ModelAdmin):
    using = 'parser'

    def save_model(self, request, obj, form, change):
        obj.save(using=self.using)

    def delete_model(self, request, obj):
        obj.delete(using=self.using)

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, using=self.using, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(db_field, request, using=self.using, **kwargs)



admin.site.register(parser, MultiDBModelAdmin)

#Костыль#
#В случае миграции БД произойдет ошибка admin.sites.AlreadyRegistered
#Закоментировать 36 строку, в с 40 строки расскоментировать
""" app_config = apps.get_app_config('parser')
models = app_config.get_models()

for model in models:
    try:
        admin.site.register(model, MultiDBModelAdmin)
    except admin.sites.AlreadyRegistered:
        pass """
    