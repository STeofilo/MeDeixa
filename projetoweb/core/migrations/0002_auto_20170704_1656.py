# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 19:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='end_datetime',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='scheduled_datetime',
        ),
        migrations.AddField(
            model_name='activity',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='activity',
            name='scheduled_day',
            field=models.CharField(choices=[('DOM', 'Domingo'), ('SEG', 'Segunda'), ('TER', 'Terça'), ('QUA', 'Quarta'), ('QUI', 'Quinta'), ('SEX', 'Sexta'), ('SAB', 'Sábado')], default='DOM', max_length=200),
        ),
        migrations.AddField(
            model_name='activity',
            name='scheduled_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
