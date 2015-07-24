# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='is_private_sector',
            field=models.BooleanField(default=False, verbose_name='private sector tariff'),
        ),
    ]
