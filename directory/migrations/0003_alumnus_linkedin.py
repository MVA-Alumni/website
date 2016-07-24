# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_alumnus_last_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnus',
            name='linkedin',
            field=models.URLField(null=True),
        ),
    ]
