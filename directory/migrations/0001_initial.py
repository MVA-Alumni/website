# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import directory.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.IntegerField(choices=[(0, b'Male'), (1, b'Female')])),
                ('photo', models.ImageField(null=True, upload_to=directory.models.upload_to_photo)),
                ('cv', models.FileField(null=True, upload_to=directory.models.upload_to_cv)),
                ('phone1', models.CharField(max_length=20, null=True)),
                ('phone2', models.CharField(max_length=20, null=True)),
                ('postal', models.CharField(max_length=160, null=True)),
                ('website', models.URLField(null=True)),
                ('presentation', models.TextField(null=True)),
                ('diploma', models.CharField(max_length=80, null=True)),
                ('company', models.CharField(max_length=160, null=True)),
                ('job', models.CharField(max_length=160, null=True)),
                ('keywords', models.CharField(max_length=1000, null=True)),
                ('privacy', models.BooleanField(default=1, choices=[(0, b'Hide name in the unauthenticated area'), (1, b'Display name in the unauthenticated area')])),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='alumnus',
            name='domain',
            field=models.ForeignKey(to='directory.Domain', null=True),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alumnus',
            name='year',
            field=models.ForeignKey(to='directory.Year'),
        ),
    ]
