# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0006_auto_20151001_0627'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='nomenclature',
            unique_together=set([('code_identifier', 'coding_sys_cd')]),
        ),
    ]
