from django.contrib import admin
from parser.models import Product as parser_db
from .models import Product as defualt_db

admin.site.register(parser_db)
admin.site.register(defualt_db)