# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 19:37
from __future__ import unicode_literals

import division_perm.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name_plural': 'Подразделения',
                'verbose_name': 'Подразделение',
            },
            bases=(division_perm.models.AccessMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('middle_name', models.CharField(blank=True, max_length=255, verbose_name='Отчество')),
                ('full_access', models.ManyToManyField(related_name='owners', to='division_perm.Division', verbose_name='Полный доступ')),
                ('read_access', models.ManyToManyField(blank=True, related_name='readers', to='division_perm.Division', verbose_name='Доступ на чтение')),
            ],
            bases=(division_perm.models.AccessMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Func',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('level', models.IntegerField(default=0, help_text='0 - минимальный уровень доступа, 9 - максимальный', verbose_name='Уровень')),
                ('is_modify', models.BooleanField(default=False, help_text='Использование функции может быть связано с изменением данных', verbose_name='Изменяет')),
            ],
            options={
                'ordering': ('-level', 'name'),
                'verbose_name_plural': 'Функции',
                'verbose_name': 'Функция',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('level', models.IntegerField(default=0, help_text='0 - минимальный уровень доступа, 9 - максимальный', verbose_name='Уровень')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='division_perm.Division', verbose_name='Подразделение')),
            ],
            options={
                'ordering': ('division', '-level', 'name'),
                'verbose_name_plural': 'Роли',
                'verbose_name': 'Роль',
            },
            bases=(division_perm.models.AccessMixin, models.Model),
        ),
        migrations.AddField(
            model_name='employee',
            name='roles',
            field=models.ManyToManyField(related_name='employees', to='division_perm.Role', verbose_name='Роли'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='division',
            name='employees',
            field=models.ManyToManyField(blank=True, related_name='divisions', to='division_perm.Employee', verbose_name='Сотрудники'),
        ),
        migrations.AddField(
            model_name='division',
            name='full_access',
            field=models.ManyToManyField(related_name='_division_full_access_+', to='division_perm.Division', verbose_name='Полный доступ'),
        ),
        migrations.AddField(
            model_name='division',
            name='read_access',
            field=models.ManyToManyField(blank=True, related_name='_division_read_access_+', to='division_perm.Division', verbose_name='Доступ на чтение'),
        ),
        migrations.AlterUniqueTogether(
            name='employee',
            unique_together=set([('last_name', 'first_name', 'middle_name')]),
        ),
    ]
