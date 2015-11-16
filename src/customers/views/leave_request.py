# -*- coding: utf-8 -*-
#
# Author: Sergey Dyachok <sergey@sdyachok.com.ua>
# Version: 1.0
# License: MIT License
#
from __future__ import unicode_literals
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.views.generic.edit import FormView

from ..forms import RequestForm


class LeaveRequestView(FormView):
    form_class = RequestForm
    template_name = 'customers/leave_request.html'
    success_url = reverse_lazy('leave_request')

    def form_valid(self, form):
        form.save()
        form.send_request()

        messages.success(self.request, _('Your request has been successfully sent.'))

        return super(LeaveRequestView, self).form_valid(form)
