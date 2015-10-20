# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0005_auto_20151001_0627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomenclature',
            old_name='hasDoc',
            new_name='isExclusive',
        ),
    ]
