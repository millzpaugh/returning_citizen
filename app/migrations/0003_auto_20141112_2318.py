# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20141112_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 23, 18, 46, 726673), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 23, 18, 46, 726707), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='search',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 23, 18, 46, 729675), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='search',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 23, 18, 46, 729702), auto_now=True),
            preserve_default=True,
        ),
    ]
