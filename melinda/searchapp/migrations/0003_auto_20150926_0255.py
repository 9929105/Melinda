# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchapp', '0002_nomenclature_coding_sys_cd'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('display', models.CharField(max_length=3000)),
                ('resource_description', models.CharField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='org_doc',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nomenclature',
            name='resource_type',
            field=models.ForeignKey(to='searchapp.ResourceType', null=True),
        ),
    ]
