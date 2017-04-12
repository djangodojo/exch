# -*- coding: utf-8 -*-


from django.contrib import admin
from app.models import Организация, Контрагент, Договор, Задача, Комментарий


class ОрганизацияAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'наименование',
        'инн',
        'image',
    )
    readonly_fields = (
        'id',
    )
    list_display = (
        'id',
        'инн',
        'наименование',
    )


class КонтрагентAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'картинка',
        'наименование',
        'инн',
        'покупатель',
        'поставщик',
    )
    readonly_fields = (
        'id',
    )
    list_display = (
        'id',
        'картинка',
        'наименование',
        'инн',
        'покупатель',
        'поставщик',
    )


class ДоговорAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'наименование',
        'номер',
        'дата',
        'организация',
        'контрагент',
    )
    readonly_fields = (
        'id',
    )
    list_display = (
        'id',
        'наименование',
        'номер',
        'дата',
        'организация',
        'контрагент',
    )


class ЗадачаAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'заголовок',
        'заказчик',
        'дата_создания',
        'описание',
    )
    readonly_fields = (
        'id',
        'дата_создания',
    )
    list_display = (
        'id',
        'заголовок',
        'заказчик',
        'дата_создания',
        'описание',
    )


class КомментарийAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'задача',
        'исполнитель',
        'дата_создания',
        'текст_комментария',
    )
    readonly_fields = (
        'id',
        'дата_создания',
    )
    list_display = (
        'id',
        'задача',
        'исполнитель',
        'дата_создания',
        'текст_комментария',
    )

admin.site.register(Организация, ОрганизацияAdmin)
admin.site.register(Контрагент, КонтрагентAdmin)
admin.site.register(Договор, ДоговорAdmin)
admin.site.register(Задача, ЗадачаAdmin)
admin.site.register(Комментарий, КомментарийAdmin)