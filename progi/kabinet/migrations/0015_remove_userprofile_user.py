# Generated by Django 4.0 on 2021-12-10 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0014_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
    ]