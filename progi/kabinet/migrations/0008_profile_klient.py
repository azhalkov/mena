# Generated by Django 4.0 on 2021-12-10 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kabinet', '0007_alter_profile_options_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='klient',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='kabinet.user'),
        ),
    ]
