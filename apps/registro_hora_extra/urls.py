from django.urls import path
from .views import Hora_extraList, \
    Hora_extraEdit, \
    Hora_extraDelete,\
    Hora_extraCreate,\
    Hora_extraEditBase, \
    UtilizouHoraExtra, \
    ExportarParaCsv



urlpatterns = [

    path('list', Hora_extraList.as_view(), name='list_hora_extra'),
    path('create/', Hora_extraCreate.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>/', Hora_extraEditBase.as_view(), name='update_hora_extra_base'),
    path('utilizou_hora_extra/<int:pk>/',
         UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('editar_funcionario/<int:pk>/', Hora_extraEdit.as_view(), name='update_hora_extra'),
    path('deletar/<int:pk>/', Hora_extraDelete.as_view(), name='delete_hora_extra'),
    path('exportar_csv', ExportarParaCsv.as_view(), name='exportar_csv'),


]