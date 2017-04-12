# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-15 13:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Задача',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('заголовок', models.CharField(max_length=100, unique=True, verbose_name='заголовок')),
                ('дата_создания', models.DateTimeField(auto_now_add=True)),
                ('описание', models.TextField(verbose_name='описание')),
                ('заказчик', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'задачи',
                'verbose_name': 'задача',
                'ordering': ('дата_создания',),
            },
        ),
        migrations.CreateModel(
            name='Комментарий',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('дата_создания', models.DateTimeField(auto_now_add=True)),
                ('текст_комментария', models.CharField(max_length=500, unique=True, verbose_name='текст комментария')),
                ('задача', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Задача', verbose_name='задача')),
                ('исполнитель', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'комментарии',
                'verbose_name': 'комментарий',
                'ordering': ('дата_создания',),
            },
        ),
    ]