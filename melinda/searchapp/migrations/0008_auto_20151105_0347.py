# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0007_auto_20151001_0806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nomenclature',
            old_name='attribute_string',
            new_name='direct_url',
        ),
    ]
