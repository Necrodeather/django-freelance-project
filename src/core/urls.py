"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from .views import index, export, check_entry, export_button, update_button

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('view/', check_entry, name='check'),
    path('parser_buttons/', include('parser.urls')),
    path('export/', export, name='export_db'),
    path('export_button/', export_button, name='export_button'),
    path('update_button/', update_button, name='update'),
]
