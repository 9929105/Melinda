# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0009_auto_20151105_0347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomenclature',
            old_name='direct_url',
            new_name='attributes',
        ),
    ]
