# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0008_auto_20151105_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nomenclature',
            name='direct_url',
            field=models.CharField(default=b'', max_length=5000),
        ),
    ]
