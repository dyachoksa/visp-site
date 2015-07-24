# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Price(models.Model):
    title = models.CharField(_('title'), max_length=50, unique=True)
    price = models.DecimalField(_('price'), max_digits=10, decimal_places=2)
    speed = models.CharField(_('speed'), max_length=25)
    description = models.TextField(_('description'), max_length=200, blank=True, null=True)
    is_published = models.BooleanField(_('is published'), default=True)
    is_private_sector = models.BooleanField(_('private sector tariff'), default=False)
    position = models.SmallIntegerField(_('position'), default=1)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        index_together = (
            ('created', 'is_published'),
            ('is_private_sector', 'position'),
            ('is_published', 'is_private_sector', 'position'),
        )
        ordering = ['is_private_sector', 'position']
        verbose_name = _('price')
        verbose_name_plural = _('prices')

    def __str__(self):
        return self.title
