# Generated by Django 5.0.3 on 2024-04-03 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_setting_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='current',
            new_name='currency',
        ),
    ]
