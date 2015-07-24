# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_price_is_private_sector'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['is_private_sector', 'position'], 'verbose_name': 'price', 'verbose_name_plural': 'prices'},
        ),
        migrations.AddField(
            model_name='price',
            name='position',
            field=models.SmallIntegerField(default=1, verbose_name='position'),
        ),
        migrations.AlterIndexTogether(
            name='price',
            index_together=set([('is_private_sector', 'position'), ('created', 'is_published'), ('is_published', 'is_private_sector', 'position')]),
        ),
    ]
