from django.contrib import admin
from bitrix.models import *
# Register your models here.

class TagatAdmin(admin.ModelAdmin):
    list_display = ('object', 'idobject', 'shortname', 'inn', 'tarif', 'idsystem', 'kpp', 'name', 'dbeg', 'dend')
    search_fields = ('object', 'idobject', 'shortname', 'inn', 'tarif', 'idsystem', 'kpp', 'name', 'dbeg', 'dend')
    list_filter = ('object', 'idobject', 'shortname', 'inn', 'tarif', 'idsystem', 'kpp', 'name', 'dbeg', 'dend')
    fieldsets = (
        (None, {'fields': ('object', 'idobject', 'shortname', 'inn', 'tarif', 'idsystem', 'kpp', 'name', 'dbeg', 'dend')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('object', 'idobject', 'shortname', 'inn', 'tarif', 'idsystem', 'kpp', 'name', 'dbeg', 'dend'),

        })
    )

class TdataAdmin(admin.ModelAdmin):
    list_display = ('login', 'idlogin', "object")
    search_fields = ('login', 'idlogin', 'idsystem', 'object')
    list_filter = ('login', 'idlogin', 'idsystem', 'object', 'idobject', 'isactive', 'id')
    list_per_page = 25
    fieldsets = (
        (None, {'fields': ('login', 'idlogin', 'idsystem', 'object')}),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('login', 'idlogin', 'idsystem', 'object', 'idobject', 'isactive', 'id'),

        })
    )


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
    
class Twialon100Admin(admin.ModelAdmin):
    list_display = ('klient', 'login', 'id')
    search_fields = ('klient', 'login', 'id')
    list_filter = ('klient', 'id','login')
    list_per_page = 25



admin.site.register(Tagat, TagatAdmin)
admin.site.register(Tdata, TdataAdmin)
admin.site.register(Temail, TemailAdmin)
admin.site.register(Tklient, TklientAdmin)
admin.site.register(Ttarif, TtarifAdmin)
admin.site.register(Twialon100, Twialon100Admin)

