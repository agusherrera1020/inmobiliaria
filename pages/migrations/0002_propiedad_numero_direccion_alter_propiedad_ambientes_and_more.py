# Generated by Django 4.2.1 on 2023-05-29 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propiedad',
            name='numero_direccion',
            field=models.IntegerField(default=0, verbose_name='Número de Dirección'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='ambientes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Ambientes'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='baños',
            field=models.IntegerField(blank=True, null=True, verbose_name='Baños'),
        ),
        migrations.AlterField(
            model_name='propiedad',
            name='habitaciones',
            field=models.IntegerField(blank=True, null=True, verbose_name='Habitaciones'),
        ),
    ]
