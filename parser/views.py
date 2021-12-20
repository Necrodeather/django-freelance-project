from django.shortcuts import render
from django.http import HttpResponseRedirect
from time import sleep
from os import chdir, system

def shutdown():
    chdir(r'/home/necrodeather/Desktop/django/parser/parsers/')
    system('ps a | grep app.py | cat > pid.txt')
    with open('/home/necrodeather/Desktop/django/parser/parsers/pid.txt', 'r') as pid:
        lines = pid.readlines()
        system(f"kill -9 {lines[0].strip()[:5]}")
    pid.close()

def index(request):
    return render(request, 'parser/index.html')

def power_button(request):
    chdir(r'/home/necrodeather/Desktop/django/parser/parsers/')
    system(r'python3 app.py')
    return HttpResponseRedirect('/admin')

def restart_button(request):
    shutdown()
    sleep(5)
    system(r'python3 app.py') 
    return HttpResponseRedirect('/admin')

def shutdown_button(request):
    shutdown()
    return HttpResponseRedirect('/admin')