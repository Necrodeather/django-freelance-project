Команды для подготовки к запуску проекта на ubuntu:
sudo apt install python3-pip
pip install django
Перед запуском заходим в директорию джанго-проекта и вводим для запуска джанго-проекта:
python3 manage.py runserver
джанго-запущен.

Если будут Варнинги о миграции, останавливаем работу проекта(ctrl+c) и вводим данные команды:
python3 manage.py migrate
python3 manage.py migrate parser
python3 manage.py migrate --database=parser
python3 manage.py makemigrations
python3 manage.py makemigrations parser
И потом запускаем проект.

В браузере вводим данный адрес, для входа в админ-панель: 
127.0.0.1:8000/admin 

Логин: user
Пароль: 1

Файлы, где надо редактировать пути директорий(В самых файлах они отмечены также комментариями)
джанго_проект/settings.py:
85-88 строка
джанго_проект/parser/views.py:
10,13,28 строка
джанго_проект/parser/export_db.py
8 строка

Изменение таблицы БД парсера в админ-панели:
джанго_проект/parser/models.py:
35-37 строка

Изменение названия админ-панели(logo)
джанго_проект/parser/admin.py:
5 строка

шаблоны под верстку админ-панели:
джанго_проект/parser/templates/admin
index.html - главная админ-панели
nav_sidebar.html - нав-сайдбар, где находятся кнопки "Работа парсера"

Для верстки, обращаться в оф.документацию django:
https://docs.djangoproject.com/en/4.0/


для CSS/JS документация:
https://docs.djangoproject.com/en/4.0/howto/static-files/
