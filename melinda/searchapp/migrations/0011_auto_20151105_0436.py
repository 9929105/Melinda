# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0010_auto_20151105_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomenclature',
            name='description',
            field=models.CharField(default=b'', max_length=10000),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='directURL',
            field=models.CharField(default=b'', max_length=5000),
        ),
    ]
