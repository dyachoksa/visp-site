# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.conf.urls import url

from .views import PriceListView


urlpatterns = [
    url(r'^$', PriceListView.as_view(), name='list'),
]
