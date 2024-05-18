# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Tagat(models.Model):

    class SystemMonitoring(models.IntegerChoices):

        WIALON_Hosting = 11, 'Wialon Hosting'
        Fort_Monitoring = 12, 'Fort Monitoring'
        Glonass_Monitoring = 13, 'Glonass Monitoring'
        Scout = 14, 'Scout'
        Era = 15, 'Era'
        WIALON_Local = 16, 'Wialon Local'

    object = models.TextField(
            blank=True, 
            null=True,
            verbose_name='Имя ТС'
            )
    idobject = models.TextField(
            blank=True, 
            null=True,
            verbose_name='ID ТС'
            )
    shortname = models.TextField(
            blank=True,
            null=True,
            verbose_name='Короткое имя Клиента',
            )
    inn = models.TextField(
            blank=True,
            null=True,
            verbose_name='ИНН',
            )
    tarif = models.IntegerField(
            blank=True, 
            null=True,
            verbose_name='Тариф',
            )
    idsystem = models.BigIntegerField(
            blank=True, 
            null=True,
            choices=SystemMonitoring.choices,
            verbose_name= 'Система мониторинга',
            )
    kpp = models.TextField(
            blank=True, 
            null=True,
            verbose_name='КПП',
            )
    name = models.TextField(
            blank=True,
            null=True,
            verbose_name='Рабочее имя Клиента',
            )
    dbeg = models.DateTimeField(
            blank=True,
            null=True,
            verbose_name='Дата начала разбивки',
            )
    dend = models.DateTimeField(
            blank=True, 
            null=True,
            verbose_name='Дата окончания разбивки',
            )

    class Meta:
        managed = False
        db_table = 'tagat'
        db_table_comment = 'Дополнительная разбивка одной учетной записи по ИНН. Впервые возникла необходимость для агат-проекта'
        verbose_name = 'Дополнительная разбивка'
        verbose_name_plural = 'Дополнительные разбивки'

    def __str__(self):
        return self.object


class Tdata(models.Model):

    class SystemMonitoring(models.IntegerChoices):

        WIALON_Hosting = 11, 'Wialon Hosting'
        Fort_Monitoring = 12, 'Fort Monitoring'
        Glonass_Monitoring = 13, 'Glonass Monitoring'
        Scout = 14, 'Scout'
        Era = 15, 'Era'
        WIALON_Local = 16, 'Wialon Local'
        

    login = models.TextField(
            blank=True,
            null=True,
            verbose_name='Клиент в системе мониторинга',
            )
    idlogin = models.TextField(
            blank=True, 
            null=True,
            verbose_name='ID клиента в системе мониторинга',
            )
    idsystem = models.IntegerField(
            blank=True,
            null=True,
            verbose_name='Система мониторинга',
            choices=SystemMonitoring.choices,
            )
    object = models.TextField(
            blank=True,
            null=True,
            verbose_name='Имя ТС',
            )
    idobject = models.TextField(
            blank=True,
            null=True,
            verbose_name='ID ТС',
            )
    isactive = models.TextField(
            blank=True, 
            null=True,
            verbose_name='Активен',
            )
    id = models.BigIntegerField(primary_key=True)
    dimport = models.DateTimeField(
            blank=True, 
            null=True,
            verbose_name='Дата выгрузки',
            )

    class Meta:
        managed = False
        db_table = 'tdata'
        verbose_name = 'Объект мониторинга'
        verbose_name_plural = 'Объекты мониторинга'

    def __str__(self):
        return self.object


class Temail(models.Model):

    email = models.TextField(
            blank=True,
            null=True,
            verbose_name='Электронная почта',
            )
    name = models.TextField(
            blank=True,
            null=True,
            verbose_name='Клиент',
            )
    inn = models.TextField(
            blank=True,
            null=True,
            verbose_name='ИНН',
            )
    kpp = models.TextField(
            blank=True, 
            null=True,
            verbose_name='КПП',
            )

    class Meta:
        managed = False
        db_table = 'temail'
        verbose_name = 'Электронная почта'
        verbose_name_plural = 'Электронные почты'

    def __str__(self):
        return self.email


class Tklient(models.Model):
    name = models.TextField(
            blank=True,
            null=True,
            verbose_name='Рабочее имя',
            )
    shortname = models.TextField(
            blank=True,
            null=True,
            verbose_name='Короткое имя',
            )
    type = models.TextField(
            blank=True,
            null=True,
            verbose_name='Тип клиента',
            )
    inn = models.TextField(
            blank=True,
            null=True,
            verbose_name='ИНН',
            )
    kpp = models.TextField(
            blank=True, 
            null=True,
            verbose_name='КПП',
            )
    id = models.BigAutoField(primary_key=True)
    tarif = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tklient'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name



class Ttarif(models.Model):
    tkid = models.ForeignKey(
            Tklient, 
            models.DO_NOTHING, 
            db_column='tkid', 
            blank=True, 
            null=True,
            verbose_name='ID Клиента',
            )
    tarif = models.DecimalField(
            max_digits=6,
            decimal_places=2,
            blank=True, 
            null=True,
            verbose_name='Тариф',
            )
    dbeg = models.DateTimeField(
            blank=True,
            null=True,
            verbose_name='Дата начала',
            )
    dend = models.DateTimeField(
            blank=True,
            null=True,
            verbose_name='Дата окончания',
            )
    id = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'ttarif'
        verbose_name = 'Тарифы'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return self.tarif


class Twialon100(models.Model):
    klient = models.TextField(
            blank=True,
            null=True,
            verbose_name='Клиент',
            )
    login = models.TextField(
            blank=True, 
            null=True,
            verbose_name='Логин',
            )
    id = models.BigAutoField(primary_key=True)
    logintd = models.TextField(
            blank=True, 
            null=True,
            verbose_name='Клиент в системе мониторинга',
            )
    tkid = models.BigIntegerField(
            blank=True, 
            null=True,
            verbose_name='ID Клиента в базе данных',
            )

    class Meta:
        managed = False
        db_table = 'twialon100'
        db_table_comment = 'Таблица учетных записей Клиента. Исторически сформированная на основания Google таблицы Wialon100. Является вспомогательной таблицей для соединения объекта мониторинга и клиента.'
        verbose_name = 'Учетная запись Клиента'
        verbose_name_plural = 'Учетные записи Клиентов'

