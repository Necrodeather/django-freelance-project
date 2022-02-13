from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .export_db import add_info
from time import sleep
from os import system
from .models import Product, CatalogProduct
from .update import update_info
from datetime import datetime
from freelance_project.settings import BASE_DIR


def index(request):
    return render(request, './index.html')


def check_entry(request):
    new_data = CatalogProduct.objects.using('parser').all()
    old_data = Product.objects.all()
    return render(request, './admin/view.html', {'old_data': old_data, 'new_data': new_data})

def shutdown():
    system(f'ps a | grep app.py | cat > {BASE_DIR}/parser/parsers/pid.txt')
    with open(f'{BASE_DIR}/parser/parsers/pid.txt', 'r') as pid:
        lines = pid.readlines()
        system(f"kill -9 {lines[0].strip()[:5]}")
    pid.close()

def start_parser(request, text_info):
    system(f'python {BASE_DIR}/parser/parsers/app.py') 
    messages.add_message(request, messages.INFO, text_info)

def power_button(request):
    print('power')
    start_parser(request, 'Включение парсера прошло успешно!')
    return HttpResponseRedirect('/admin')

def restart_button(request):
    print('restart')
    shutdown()
    sleep(5)
    HttpResponseRedirect('/admin')
    return start_parser(request, 'Перезагрузка парсера прошло успешно!')

def shutdown_button(request):
    print('shutdown')
    shutdown()
    messages.add_message(request, messages.INFO, 'Выключение парсера прошло успешно!')
    return HttpResponseRedirect('/admin')

def export_button(request):
    print('export')
    adding = add_info()
    adding.add_table()
    adding.add_images()
    messages.add_message(request, messages.INFO, 'Перенес в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin')

def update_button(request):
    update = update_info()
    date = str(datetime.today())
    system(f'copy db.sqlite3 {BASE_DIR}/backupdb/')
    update.select_sku()
    messages.add_message(request, messages.INFO, 'Изменение в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin')