# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_handled',
            field=models.BooleanField(default=False, verbose_name='is handled'),
        ),
        migrations.AlterField(
            model_name='request',
            name='customer_name',
            field=models.CharField(max_length=150, verbose_name='name'),
        ),
    ]
