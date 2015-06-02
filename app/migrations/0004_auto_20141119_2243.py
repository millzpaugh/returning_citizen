# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20141112_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 19, 22, 43, 0, 673156), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 19, 22, 43, 0, 673186), auto_now=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='search',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 19, 22, 43, 0, 674996), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='search',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 19, 22, 43, 0, 675024), auto_now=True),
            preserve_default=True,
        ),
    ]
