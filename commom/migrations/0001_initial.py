# Generated by Django 3.2.9 on 2022-01-10 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da província.', max_length=15, unique=True)),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome do município.', max_length=20, unique=True)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commom.province', verbose_name='the related province')),
            ],
            options={
                'verbose_name': 'County',
                'verbose_name_plural': 'Counties',
                'ordering': ['name'],
                'unique_together': {('name', 'province')},
            },
        ),
    ]
