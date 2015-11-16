# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Request


class RequestsAdmin(admin.ModelAdmin):
    list_display = ['request_date', 'customer_name', 'address', 'phone']


admin.site.register(Request, RequestsAdmin)
