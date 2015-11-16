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
from model_utils.models import TimeStampedModel


@python_2_unicode_compatible
class Request(TimeStampedModel):
    request_date = models.DateTimeField(_('request date'), auto_now_add=True)
    customer_name = models.CharField(_('name'), max_length=150)
    address = models.CharField(_('address'), max_length=255)
    phone = models.CharField(_('phone number'), max_length=25)
    customer_comment = models.TextField(_('comment'), blank=True, default=None, null=True)

    class Meta:
        ordering = ['-created']
        verbose_name = _('request')
        verbose_name_plural = _('requests')

    def __str__(self):
        return 'Request object'
