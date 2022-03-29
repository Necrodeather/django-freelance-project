from django.contrib import admin
from parser.models import Product as parser_db
from info.models import Product as info_db

admin.site.register(parser_db)
admin.site.register(info_db)