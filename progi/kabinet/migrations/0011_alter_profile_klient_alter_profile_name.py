# Generated by Django 4.0 on 2021-12-10 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0010_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='klient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kabinet.user'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Псевдоним'),
        ),
    ]