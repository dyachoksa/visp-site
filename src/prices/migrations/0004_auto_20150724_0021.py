# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0003_auto_20150723_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='speed',
            field=models.CharField(max_length=25, verbose_name='speed'),
        ),
    ]
