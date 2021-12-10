# Generated by Django 4.0 on 2021-12-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0002_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_activ', models.BooleanField(default=False, verbose_name='Активность')),
                ('strana', models.CharField(default='Россия', max_length=80, verbose_name='Страна')),
                ('gorod', models.CharField(default='Россия', max_length=80, verbose_name='Город')),
                ('raion', models.CharField(default='Россия', max_length=80, verbose_name='Район')),
                ('ulica', models.CharField(default='Россия', max_length=80, verbose_name='Улица')),
                ('n_doma', models.SmallIntegerField(default='------', max_length=10, verbose_name='Номер дома № :')),
                ('n_podezda', models.SmallIntegerField(default='------', max_length=10, verbose_name='Номер подъезда № :')),
                ('n_kvartiri', models.SmallIntegerField(default='------', max_length=10, verbose_name='Номер квартиры № :')),
                ('pochta_index', models.SmallIntegerField(default='------', max_length=80, verbose_name='Почтовый индекс')),
                ('zametka', models.CharField(default='-', max_length=80, verbose_name='Для заметок')),
                ('data_start', models.DateTimeField(auto_now=True, verbose_name='Дата подачи')),
                ('data_stop', models.DateTimeField(verbose_name='Дата снятия')),
                ('slug', models.SlugField(default='-', verbose_name='Слаг')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
    ]