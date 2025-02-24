#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
from django.core.management import call_command
from django.db import IntegrityError

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Movie.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def load_data():
    try:
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            call_command('loaddata', 'data.json')
    except IntegrityError as e:
        print(f"Error loading data: {e}")
    except UnicodeDecodeError as e:
        print(f"Encoding error: {e}")

if __name__ == "__main__":
    main()
    load_data()
