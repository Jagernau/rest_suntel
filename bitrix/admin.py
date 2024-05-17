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


class TdataAdmin(admin.ModelAdmin):
    list_display = ('object', 'login', 'idlogin', "dimport")
    search_fields = ('login', 'idlogin', 'idsystem', 'object')
    list_filter = (('dimport', DateFieldListFilter), )

    list_per_page = 20

    def get_clients(self, obj):
        if obj.login:
            if Twialon100.objects.filter(login=obj.login).exists():
                twialon100_tkid= Twialon100.objects.filter(login=obj.login).first().tkid
                if tklient := Tklient.objects.filter(id=twialon100_tkid).first():
                    return tklient.name


class TemailAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'inn', 'kpp')
    search_fields = ('email', 'name', 'inn', 'kpp')
    list_filter = ('email', 'name', 'inn', 'kpp')
    fieldsets = (
        (None, {'fields': ('email', 'name', 'inn', 'kpp')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'inn', 'kpp'),

        })
    )

class TklientAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortname', 'type')
    search_fields = ('name', 'shortname', 'type')
    list_filter = ('name', 'shortname', 'type')
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
    list_display = ("tarif",)
    search_fields = ('tarif', 'id')
    list_filter = ('tarif',)
    list_per_page = 25
    

admin.site.register(Tagat, TagatAdmin)
admin.site.register(Tdata, TdataAdmin)
admin.site.register(Temail, TemailAdmin)
admin.site.register(Tklient, TklientAdmin)
admin.site.register(Ttarif, TtarifAdmin)

