# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0004_auto_20150926_0311'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomenclature',
            old_name='org_doc',
            new_name='hasDoc',
        ),
    ]
