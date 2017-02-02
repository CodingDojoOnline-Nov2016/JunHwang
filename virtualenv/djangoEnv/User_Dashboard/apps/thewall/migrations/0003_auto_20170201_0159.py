# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0002_users_description'),
        ('thewall', '0002_auto_20170131_2313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='master_id',
        ),
        migrations.AddField(
            model_name='messages',
            name='master_id',
            field=models.ManyToManyField(related_name='masterofmessage', to='login_reg.Users'),
        ),
        migrations.RemoveField(
            model_name='messages',
            name='user_id',
        ),
        migrations.AddField(
            model_name='messages',
            name='user_id',
            field=models.ManyToManyField(related_name='userofmessage', to='login_reg.Users'),
        ),
    ]