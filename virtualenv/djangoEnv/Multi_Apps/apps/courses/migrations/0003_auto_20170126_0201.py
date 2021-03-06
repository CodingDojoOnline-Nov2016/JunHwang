# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 02:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0001_initial'),
        ('courses', '0002_courses_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='user',
        ),
        migrations.AddField(
            model_name='courses',
            name='account',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='login_reg.Users'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
