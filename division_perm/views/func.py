# coding: utf-8
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from djutils.views.generic import TitleMixin
from ..generic import FuncAccessMixin
from .. import models
from .. import consts


class List(TitleMixin, FuncAccessMixin, LoginRequiredMixin, generic.ListView):
    func_code = consts.SYS_READ_FUNC
    title = 'Функции'
    model = models.Func


class Detail(TitleMixin, FuncAccessMixin, LoginRequiredMixin, generic.DetailView):
    func_code = consts.SYS_READ_FUNC
    model = models.Func

    def get_title(self):
        return 'Функция "%s"' % self.get_object().name
