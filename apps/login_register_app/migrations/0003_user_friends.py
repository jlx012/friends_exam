# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-28 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register_app', '0002_auto_20170724_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='_user_friends_+', to='login_register_app.User'),
        ),
    ]
