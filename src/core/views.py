from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from parser.methods import add_info
from parser.models import Product as parser
from info.models import Product as info
from parser.methods import update_info

def index(request):
    return render(request, './index.html')

def export(request):
    export_data = info.objects.filter(unique = False)
    return render(request, './admin/export.html', {'export_data': export_data})
    
def export_button(request):
    adding = add_info()
    adding.add_table()
    adding.add_images()
    messages.add_message(request, messages.INFO, 'Перенес в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin')

def check_entry(request):
    new_data = parser.objects.all()
    old_data = info.objects.all()
    return render(request, './admin/view.html', {'old_data': old_data, 'new_data': new_data})

def update_button(request):
    #call_command('dbbackup')
    update = update_info()
    date = str(datetime.today())
    update.select_sku()
    messages.add_message(request, messages.INFO, 'Изменение в основную базу прошло успешно!')
    return HttpResponseRedirect('/admin')