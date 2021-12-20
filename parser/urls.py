from django.conf.urls import url
from django.urls import path
from .admin import admin_site

from . import views

urlpatterns = [
    url(r'^admin/', admin_site.site.urls),
    path('', views.parser, name='parser')
]