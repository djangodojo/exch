# -*- coding: utf-8 -*-


from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from jsonrpc import jsonrpc_method
from app.models import Задача, Комментарий


def index(request):
    return render(request, 'app/base.html')
    #return HttpResponse("Hello, world. You're at the polls index.")


@jsonrpc_method('app.get_task_list', authenticated=True)
def get_task_list(request):

    задачи = Задача.objects.all()
    список = []
    for задача in задачи:
        элем = {}
        элем['id'] = задача.id
        элем['заголовок'] = задача.заголовок

        заказчик = {}
        заказчик['id'] = задача.заказчик.id
        заказчик['имя'] = задача.заказчик.first_name
        заказчик['фамилия'] = задача.заказчик.last_name

        элем['заказчик'] = заказчик
        элем['дата_создания'] = задача.дата_создания
        элем['описание'] = задача.описание
        список.append(элем)

    return список


@jsonrpc_method('app.get_task_with_comments', authenticated=True)
def get_task_with_comments(request, id):

    задача = Задача.objects.get(id=id)
    объект = {}
    объект['id'] = задача.id
    объект['заголовок'] = задача.заголовок

    заказчик = {}
    заказчик['id'] = задача.заказчик.id
    заказчик['имя'] = задача.заказчик.first_name
    заказчик['фамилия'] = задача.заказчик.last_name

    объект['заказчик'] = заказчик
    объект['дата_создания'] = задача.дата_создания
    объект['описание'] = задача.описание

    комментарии = Комментарий.objects.filter(задача=задача)
    список_комментов = []
    for комментарий in комментарии:

        элем = {}
        элем['дата_создания'] = комментарий.дата_создания
        элем['текст_комментария'] = комментарий.текст_комментария

        исполнитель = {}
        исполнитель['id'] = комментарий.исполнитель.id
        исполнитель['имя'] = комментарий.исполнитель.first_name
        исполнитель['фамилия'] = комментарий.исполнитель.last_name

        элем['исполнитель'] = исполнитель
        список_комментов.append(элем)

    объект['комментарии'] = список_комментов

    return объект


@jsonrpc_method('app.create_task', authenticated=True)
def create_task(request, title, description):

    задача = Задача()
    задача.заголовок = title
    задача.описание = description
    задача.заказчик = request.user
    задача.save()


@jsonrpc_method('app.create_comment', authenticated=True)
def create_comment(request, id, comment):

    задача = Задача.objects.get(id=id)

    комментарий = Комментарий()
    комментарий.задача = задача
    комментарий.исполнитель = request.user
    комментарий.текст_комментария = comment
    комментарий.save()

