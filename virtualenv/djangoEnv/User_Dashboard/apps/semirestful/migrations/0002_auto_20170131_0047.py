# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 00:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('semirestful', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userlevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_level', models.PositiveSmallIntegerField()),
            ],
            managers=[
                ('usermanager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
