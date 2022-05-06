from django.http import HttpResponseRedirect
from django.contrib import messages
from .tasks import start_parser_task

def start_parser(request, text_info):
    start_parser_task.delay()
    messages.add_message(request, messages.INFO, text_info)

def power_button(request):
    start_parser(request, 'Включение парсера прошло успешно!')
    return HttpResponseRedirect('/admin')

def restart_button(request):
    start_parser(request, 'Перезагрузка парсера прошла успешно!')
    return HttpResponseRedirect('/admin')

def shutdown_button(request):
    messages.add_message(request, messages.INFO, 'Выключение парсера прошло успешно!')
    return HttpResponseRedirect('/admin')



