# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 14, 5, 8, 647227), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 14, 5, 8, 647257), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='search',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 14, 5, 8, 649224), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='search',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 12, 14, 5, 8, 649252), auto_now=True),
            preserve_default=True,
        ),
    ]
