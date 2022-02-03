from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .export_db import add_info
from time import sleep
from os import chdir, system
from .models import Product, CatalogProduct
from .update import update_info
from datetime import datetime


def index(request):
    return render(request, './index.html')


def check_entry(request):
    new_data = CatalogProduct.objects.using('parser').all()
    old_data = Product.objects.all()
    return render(request, './admin/view.html', {'old_data': old_data, 'new_data': new_data})

def shutdown():
    #Редактировать путь до каталога парсера
    chdir(r'/home/necrodeather/Desktop/Wyrestorm-django/parser/parsers/')
    system('ps a | grep app.py | cat > pid.txt')
    #Редактировать путь до каталога парсера, чтобы pid.txt сохранялся там
    with open('/home/necrodeather/Desktop/Wyrestorm-django/parser/parsers/pid.txt', 'r') as pid:
        lines = pid.readlines()
        system(f"kill -9 {lines[0].strip()[:5]}")
    pid.close()

def start_parser(request, text_info):
    system(r'python app.py') 
    messages.add_message(request, messages.INFO, f'{text_info}')

def power_button(request):
    print('power')
    #Редактировать путь до каталога парсера
    chdir(r'C:\Users\Necrodeather\Desktop\django-freelance-project\parser\parsers')
    start_parser(request, 'Включение парсера прошло успешно!')
    return HttpResponseRedirect('/admin')

def restart_button(request):
    print('restart')
    shutdown()
    sleep(5)
    start_parser(request, 'Перезагрузка парсера прошло успешно!')
    return HttpResponseRedirect('/admin')

def shutdown_button(request):
    print('shutdown')
    shutdown()
    messages.add_message(request, messages.INFO, 'Выключение парсера прошло успешно!')
    return HttpResponseRedirect('/admin')

def export_button(request):
    print('export')
    delete = add_info
    delete.add_table()
    messages.add_message(request, messages.INFO, 'Перенес в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin')

def update_button(request):
    update = update_info()
    date = str(datetime.today())
    system(r'copy db.sqlite3 C:\Users\Necrodeather\Desktop\django-freelance-project\backupdb')
    update.select_sku()
    messages.add_message(request, messages.INFO, 'Изменение в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin')