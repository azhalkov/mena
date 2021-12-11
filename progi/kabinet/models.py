# progi/kabinet/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from transliterate import slugify
from django.conf import settings


#  AUTH_USER_MODEL = 'progi.
#  models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='User')
#  Create your models here.
from seting.settings import AUTH_USER_MODEL


class User(AbstractUser):

    zametka = models.TextField(max_length=500, verbose_name='Заметки',
                               blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']


class Status(models.Model):

    title = models.CharField('Роль', max_length=100, default='-')
    is_activ = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Adres(models.Model):

    is_activ = models.BooleanField(verbose_name='Активность', default=False)
    strana = models.CharField(max_length=80, verbose_name='Страна', default='Россия')
    gorod = models.CharField(max_length=80, verbose_name='Город', default='Павловская')
    raion = models.CharField(max_length=80, verbose_name='Район', default='Район')
    ulica = models.CharField(max_length=80, verbose_name='Улица', default='Улица')
    n_doma = models.SmallIntegerField(verbose_name='Номер дома № :', default='------')
    n_podezda = models.SmallIntegerField(verbose_name='Номер подъезда № :', blank=True, null=True)
    n_kvartiri = models.SmallIntegerField(verbose_name='Номер квартиры № :', blank=True, null=True)
    pochta_index = models.SmallIntegerField(verbose_name='Почтовый индекс', default='------')
    zametka = models.CharField(max_length=80, verbose_name='Для заметок', default='-')
    data_start = models.DateTimeField(verbose_name='Дата подачи', auto_now_add=True, blank=True, null=True)
    data_stop = models.DateTimeField(verbose_name='Дата снятия', auto_now=True, blank=True, null=True)
    slug = models.SlugField(verbose_name='Слаг', default='-')

    def __str__(self):
        return '%s' % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify('u-{}_d-{}_p-{}_k-{}'.format(self.ulica, self.n_doma, self.n_podezda, self.n_kvartiri))
        super(Adres, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class UserProfile(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=128, verbose_name='Псевдоним', blank=True, null=True)
    avatar = models.ImageField(verbose_name='Миниатюра', upload_to='image/avatar/', blank=True, null=True)

    def __str__(self):
        return '%s' % self.name


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'





