# -*- coding: utf-8 -*-


from django.db import models
from django.contrib.auth.models import User


class Организация(models.Model):

    наименование = models.CharField(
        max_length=100,
        verbose_name='наименование',
    )
    инн = models.CharField(
        max_length=12,
        verbose_name='инн',
    )
    image = models.ImageField(
        upload_to='images',
        verbose_name='картинка',
    )
    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'организации'
        ordering = (
            'id',
        )

    def __str__(self):
        return str(self.наименование)


class Контрагент(models.Model):

    наименование = models.CharField(
        max_length=100,
        verbose_name='наименование',
    )
    инн = models.CharField(
        max_length=12,
        verbose_name='инн',
    )
    покупатель = models.BooleanField(
        verbose_name='покупатель',
    )
    поставщик = models.BooleanField(
        verbose_name='поставщик',
    )
    картинка = models.ImageField(
        verbose_name='картинка',
    )

    class Meta:
        verbose_name = 'контрагент'
        verbose_name_plural = 'контрагенты'
        ordering = (
            'id',
        )

    def __str__(self):
        return str(self.наименование)


class Договор(models.Model):

    наименование = models.CharField(
        max_length=100,
        verbose_name='наименование',
    )
    номер = models.CharField(
        max_length=100,
        verbose_name='номер',
    )
    дата = models.DateField(
        verbose_name='дата',
    )
    организация = models.ForeignKey(
        Организация,
        verbose_name='организация',
    )
    контрагент = models.ForeignKey(
        Контрагент,
        verbose_name='контрагент',
    )

    class Meta:
        verbose_name = 'договор'
        verbose_name_plural = 'договоры'
        ordering = (
            'id',
        )

    def __str__(self):
        return str(self.наименование)


class Задача(models.Model):
    #id будет создан автоматически
    заголовок = models.CharField(max_length=100,
                                 unique=True,
                                 verbose_name='заголовок')
    заказчик = models.ForeignKey(User, on_delete=models.CASCADE)
    дата_создания = models.DateTimeField(auto_now_add=True)
    описание = models.TextField('описание')

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = '_задачи'
        ordering = ('дата_создания',)

    def __str__(self):
        return str(self.заголовок)


class Комментарий(models.Model):
    #id будет создан автоматически
    задача = models.ForeignKey(Задача,
                               on_delete=models.CASCADE,
                               verbose_name='задача')
    исполнитель = models.ForeignKey(User, on_delete=models.CASCADE)
    дата_создания = models.DateTimeField(auto_now_add=True)
    текст_комментария = models.TextField('текст комментария')

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = '_комментарии'
        ordering = ('дата_создания',)

    def __str__(self):
        return str(self.текст_комментария)