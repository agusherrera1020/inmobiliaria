# Generated by Django 4.2.1 on 2023-06-21 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_rename_numero_inmobiliaria_propiedad_telefono_inmobiliaria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propiedad',
            name='inmobiliaria',
        ),
    ]