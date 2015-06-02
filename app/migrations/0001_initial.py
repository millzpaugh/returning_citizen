# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=140)),
                ('latitude', models.FloatField(default=0, null=True, blank=True)),
                ('longitude', models.FloatField(default=0, null=True, blank=True)),
                ('phone', models.CharField(max_length=20, null=True)),
                ('is_headquarters', models.BooleanField(default=False)),
                ('hours_open', models.CharField(max_length=200, null=True)),
                ('population', models.CharField(max_length=2000, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 51, 20, 407484), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 51, 20, 407516), auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=20000, null=True)),
                ('url', models.CharField(max_length=2000, null=True)),
                ('population_served', models.CharField(max_length=2000, null=True)),
                ('eligibility', models.CharField(max_length=2000, null=True)),
                ('programs', models.CharField(max_length=2000, null=True)),
                ('language_services', models.CharField(max_length=2000, null=True)),
                ('services', models.CharField(max_length=2000, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('location', models.CharField(max_length=255)),
                ('resource', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 51, 20, 409534), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2014, 11, 9, 18, 51, 20, 409585), auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ZipcodeCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zipcode', models.CharField(max_length=10)),
                ('latitude', models.FloatField(default=0)),
                ('longitude', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='location',
            name='provider',
            field=models.ForeignKey(to='app.Provider'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='resources_available',
            field=models.ManyToManyField(to='app.Resource'),
            preserve_default=True,
        ),
    ]
