# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0003_auto_20150926_0255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nomenclature',
            name='resource_type',
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='attribute_string',
            field=models.CharField(default=b'{}', max_length=5000),
        ),
        migrations.DeleteModel(
            name='ResourceType',
        ),
    ]
