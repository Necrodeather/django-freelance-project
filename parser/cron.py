from os import system
from pathlib import Path
from django.core.management import call_command

APP_DIR = Path(__file__).resolve().parent

def backup_db():
    call_command('dbbackup')
    system(f'python {APP_DIR}/parsers/app.py')
