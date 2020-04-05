from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresas


class EmpresaCreate(CreateView):
    model = Empresas
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('ok')

class EmpresaEdit(UpdateView):
    model = Empresas
    fields = ['nome']


