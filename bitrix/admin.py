from django.contrib import admin
from bitrix.models import *
from django.contrib.admin import DateFieldListFilter
# Register your models here.

class TagatAdmin(admin.ModelAdmin):
    list_display = ('object', 'name', 'shortname', 'inn', 'kpp', 'tarif', 'idobject', 'idsystem','dbeg', 'dend')
    search_fields = ('object', 'idobject', 'shortname', 'inn', 'tarif', 'idsystem', 'kpp', 'name', 'dbeg', 'dend')
    list_filter = ('idsystem',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': 
            (
                'object', 
                'idobject', 
                'shortname',
                'inn', 
                'tarif', 
                'idsystem', 
                'kpp',
                'name', 
                'dbeg',
                'dend'),

        })
    )
    list_per_page = 20
    date_hierarchy = 'dbeg'



class TdataAdmin(admin.ModelAdmin):
    list_display = ('object',
                    'idsystem',
                    'get_clients',
                    'login',
                    "dimport"
                    )
    search_fields = ('login', 'idlogin', 'idsystem', 'object')
    list_filter = (('dimport', DateFieldListFilter), )

    list_per_page = 20

    def get_clients(self, obj):
        if obj.login:
            if Twialon100.objects.filter(login=obj.login).exists():
                twialon100_tkid= Twialon100.objects.filter(login=obj.login).first().tkid
                if tklient := Tklient.objects.filter(id=twialon100_tkid).first():
                    return tklient.name

    get_clients.short_description = 'Клиент в 1с'
    date_hierarchy = 'dimport'

class TemailAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'inn', 'kpp')
    search_fields = ('email', 'name', 'inn', 'kpp')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'inn', 'kpp'),

        })
    )

    list_per_page = 25

class TklientAdmin(admin.ModelAdmin):
    list_display = (
            'name', 
            'shortname', 
            'type', 
            'inn',
            'kpp',
            )
    search_fields = (
            'name', 
            'shortname',
            'type', 
            'inn', 
            'kpp',
            )
    list_filter = ('type',)
    list_per_page = 25
    fieldsets = (
        (None, {'fields': ('name', 'shortname', 'type')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'shortname', 'type'),

        })
    )


class TtarifAdmin(admin.ModelAdmin):
    list_display = (
            "get_clients",
            "tarif",
            "dbeg",
            "dend",
            "get_inn",
            "get_kpp",
            )
    search_fields = ('tarif', 
                     'get_clients',
                     'get_inn',
                     'get_kpp',
                     )
    list_filter = ('tarif',)
    list_per_page = 25
    date_hierarchy = 'dbeg'


    def get_clients(self, obj):
        """Выводим клиента id клиенто тарифу"""
        if obj.tkid:
                return obj.tkid.name
    def get_inn(self, obj):
        """Выводим клиента id клиенто тарифу"""
        if obj.tkid:
                return obj.tkid.inn
    def get_kpp(self, obj):
        """Выводим клиента id клиенто тарифу"""
        if obj.tkid:
                return obj.tkid.kpp

    get_clients.short_description = 'Клиент в 1с'
    get_inn.short_description = 'ИНН Клиента'
    get_kpp.short_description = 'КПП Клиента'

class Wialon100Admin(admin.ModelAdmin):
    list_display = (
            'get_client_onec',
            'klient',
            'login',
            'tkid',
            'logintd',
            'tkid',
                    )
    search_fields = ('login', 'tkid', 'klient', 'logintd', 'get_client_onec')
    list_filter = ('login', 'tkid')
    def get_client_onec(self, obj):
        """Выводим клиента как в 1с по id"""
        if obj.tkid:
                if tklient := Tklient.objects.filter(id=obj.tkid).first():
                    return tklient.name

    get_client_onec.short_description = 'Клиент как в 1с'
    list_per_page = 25
    

admin.site.register(Tagat, TagatAdmin)
admin.site.register(Tdata, TdataAdmin)
admin.site.register(Temail, TemailAdmin)
admin.site.register(Tklient, TklientAdmin)
admin.site.register(Ttarif, TtarifAdmin)
admin.site.register(Twialon100, Wialon100Admin)

