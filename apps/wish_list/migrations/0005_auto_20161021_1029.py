# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wish_list', '0004_auto_20161021_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='wish',
            name='item_id',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
