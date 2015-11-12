# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0011_auto_20151105_0436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomenclature',
            old_name='directURL',
            new_name='url',
        ),
    ]
