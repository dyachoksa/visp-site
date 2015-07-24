# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PagesAppConfig(AppConfig):
    name = 'pages'
    verbose_name = _('Pages')

    def ready(self):
        from sitetree.sitetreeapp import register_i18n_trees
        register_i18n_trees(['main', 'pages'])
