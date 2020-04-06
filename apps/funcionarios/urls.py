from django.urls import path
from .views import FuncionarioList, \
    FuncionarioEdit, \
    FuncionarioDelete,\
    FuncionarioNovo


urlpatterns = [

    path('list', FuncionarioList.as_view(), name = 'list_funcionarios'),
    path('create/', FuncionarioNovo.as_view(), name = 'create_funcionarios'),

    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionarios'),


]