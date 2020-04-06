from django.urls import reverse_lazy
from django.views.generic import \
    ListView, \
    UpdateView, \
    DeleteView, \
    CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm

class Hora_extraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class Hora_extraEdit(UpdateView):
    model = RegistroHoraExtra

    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(Hora_extraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class Hora_extraDelete(DeleteView):
    model =RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class Hora_extraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(Hora_extraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


