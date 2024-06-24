#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import json
import django


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    django.setup()
    try:
        from shop.models import Category, Collection, Slider
        files_path = [
            'databases/categories.json',
            'databases/collections.json',
            'databases/sliders.json',
        ]
        models = {
            'categories': Category,
            'collections': Collection,
            'sliders': Slider,
        }

        for file_path in files_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                entity = file_path.split('/')[1].split('.')[0]
                model = models.get(entity)

                if model :
                    data = json.load(file)
                    for item in data:
                        header = item.get('header', [])
                        rows = item.get('rows', [])
                        for row in rows:
                            entry_data = {header[i]: row[i]  for i in range(1, len(header))}
                            model.objects.create(**entry_data)
                else:
                    print(f"Model '{entity}' not found.")

    except ImportError as exc:
        print(exc)
        sys.ecit(1)


if __name__ == '__main__':
    main()
