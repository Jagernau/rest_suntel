# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Tagat(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    object = models.TextField(blank=True, null=True)
    idobject = models.TextField(blank=True, null=True)
    shortname = models.TextField(blank=True, null=True)
    inn = models.TextField(blank=True, null=True)
    tarif = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    idsystem = models.BigIntegerField(blank=True, null=True)
    kpp = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    dbeg = models.DateTimeField(blank=True, null=True)
    dend = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.shortname

    class Meta:
        managed = False
        db_table = 'tagat'
        db_table_comment = 'Дополнительная разбивка одной учетной записи по ИНН. Впервые возникла необходимость для агат-проекта'


class Tdata(models.Model):
    login = models.TextField(blank=True, null=True)
    idlogin = models.TextField(blank=True, null=True)
    idsystem = models.IntegerField(blank=True, null=True)
    object = models.TextField(blank=True, null=True)
    idobject = models.TextField(blank=True, null=True)
    isactive = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    dimport = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.object

    class Meta:
        managed = False
        db_table = 'tdata'


class Temail(models.Model):
    id = models.BigAutoField(primary_key=True, auto_created=True)
    email = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    inn = models.TextField(blank=True, null=True)
    kpp = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        managed = False
        db_table = 'temail'


class Tklient(models.Model):
    name = models.TextField(blank=True, null=True)
    shortname = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    inn = models.TextField(blank=True, null=True)
    kpp = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    tarif = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'tklient'



class Ttarif(models.Model):
    tkid = models.ForeignKey(Tklient, models.DO_NOTHING, db_column='tkid', blank=True, null=True)
    tarif = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dbeg = models.DateTimeField(blank=True, null=True)
    dend = models.DateTimeField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.tkid

    class Meta:
        managed = False
        db_table = 'ttarif'


class Twialon100(models.Model):
    klient = models.TextField(blank=True, null=True)
    login = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)
    logintd = models.TextField(blank=True, null=True)
    tkid = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.login

    class Meta:
        managed = False
        db_table = 'twialon100'
        db_table_comment = 'Таблица учетных записей Клиента. Исторически сформированная на основания Google таблицы Wialon100. Является вспомогательной таблицей для соединения объекта мониторинга и клиента.'
