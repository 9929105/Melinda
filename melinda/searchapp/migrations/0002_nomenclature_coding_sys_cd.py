# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nomenclature',
            name='coding_sys_cd',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
