from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .export_db import delete_info
from time import sleep
from os import chdir, system

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
    messages.add_message(request, messages.INFO, f'{text_info}')
    system(r'python3 app.py') 

def index(request):
    return render(request, 'parser/index.html')

def power_button(request):
    print('power')
    #Редактировать путь до каталога парсера
    chdir(r'/home/necrodeather/Desktop/Wyrestorm-django/parser/parsers/')
    start_parser(request, 'Включение парсера прошло успешно!')
    return HttpResponseRedirect('/admin/parser/wyrestormitemsupdate/')

def restart_button(request):
    print('restart')
    shutdown()
    sleep(5)
    start_parser(request, 'Перезагрузка парсера прошло успешно!')
    return HttpResponseRedirect('/admin/parser/wyrestormitemsupdate/')

def shutdown_button(request):
    print('shutdown')
    shutdown()
    messages.add_message(request, messages.INFO, 'Выключение парсера прошло успешно!')
    return HttpResponseRedirect('/admin/parser/wyrestormitemsupdate/')

def export_button(request):
    print('export')
    delete = delete_info('wyrestorm_items','wyrestorm_items_update')
    delete.delete()
    messages.add_message(request, messages.INFO, 'Перенес в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin/parser/wyrestormitemsupdate/')