# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Price


class PricesAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']

    list_display = [
        'title', 'price', 'speed',
        'is_private_sector', 'is_published',
        'position', 'created', 'modified'
    ]
    list_display_links = ['title', 'price', 'speed']
    list_filter = ['is_private_sector', 'is_published', 'created']

    readonly_fields = ['created', 'modified']


admin.site.register(Price, PricesAdmin)
