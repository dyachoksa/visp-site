# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from captcha.fields import ReCaptchaField
from django.conf import settings
from django.core.mail import send_mail
from django.forms import ModelForm
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from .models import Request


class RequestForm(ModelForm):
    captcha = ReCaptchaField(label='')

    class Meta:
        model = Request
        fields = ['customer_name', 'address', 'phone', 'customer_comment']

    def send_request(self):
        content = render_to_string('mail/new_request.txt', {'data': self.cleaned_data})

        send_mail(_('New request'), content, 'requests@visp.com.ua', settings.REQUEST_RECIPIENTS, fail_silently=True)
