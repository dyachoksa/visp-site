# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.views.generic import ListView

from .models import Price


class PriceListView(ListView):
    model = Price
    context_object_name = 'prices'

    def get_queryset(self):
        return Price.objects.filter(is_published=True)
