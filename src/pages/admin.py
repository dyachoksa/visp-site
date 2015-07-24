# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin as BaseFlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from .admin_form import FlatPageForm


class FlatPageAdmin(BaseFlatPageAdmin):
    form = FlatPageForm


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)
