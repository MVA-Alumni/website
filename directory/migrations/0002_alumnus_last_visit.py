# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnus',
            name='last_visit',
            field=models.DateTimeField(null=True),
        ),
    ]
