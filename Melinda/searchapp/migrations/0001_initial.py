# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code_identifier', models.CharField(max_length=100)),
                ('coding_system', models.CharField(max_length=100)),
                ('display', models.CharField(max_length=2000)),
                ('popularity', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Textmap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('free_text', models.CharField(max_length=1000)),
                ('nomenclature', models.ForeignKey(to='searchapp.Nomenclature')),
            ],
        ),
    ]
