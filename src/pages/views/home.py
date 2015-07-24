# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
