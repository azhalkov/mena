# Generated by Django 4.0 on 2021-12-10 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0011_alter_profile_klient_alter_profile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='klient',
            new_name='myuser',
        ),
    ]
