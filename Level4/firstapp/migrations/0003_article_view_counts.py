# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-27 02:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_auto_20161227_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='view_counts',
            field=models.IntegerField(default=0),
        ),
    ]
