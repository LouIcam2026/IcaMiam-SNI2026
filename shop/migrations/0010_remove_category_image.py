# Generated by Django 5.0.3 on 2024-04-08 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_navcollection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]
