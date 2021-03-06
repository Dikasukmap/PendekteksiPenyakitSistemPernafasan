# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-05-12 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTB', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='DEFAULT_VALUE', max_length=128, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='no_Telepon',
            field=models.CharField(default='DEFAULT_VALUE', max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='DEFAULT_VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='retype_Password',
            field=models.CharField(default='DEFAULT_VALUE', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='DEFAULT_VALUE', max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default='DEFAULT_VALUE', help_text='*Email Harus Aktif', max_length=254, unique=True),
        ),
    ]
