# Generated by Django 4.2.2 on 2023-07-04 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('imagen', models.ImageField(upload_to='projects', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha modificacion')),
            ],
        ),
    ]
