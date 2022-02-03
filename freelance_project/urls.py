"""freelance_project URL Configuration

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
from django.urls import path
from parser import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('view/', views.check_entry, name = 'check'),
    path('update_button/', views.update_button, name='update'),
    path('shutdown_button/', views.shutdown_button, name = 'shutdown'),
    path('restart_button/', views.restart_button, name = 'restart'),
    path('power_button/', views.power_button, name = 'power'),
    path('export_button/', views.export_button, name = 'export'),
]
