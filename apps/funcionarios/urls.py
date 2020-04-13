from django.urls import path
from .views import FuncionarioList, \
    FuncionarioEdit, \
    FuncionarioDelete,\
    FuncionarioNovo,\
    Pdf, PdfDebug


from .views import pdf_reportlab, relatorio_funcionarios

urlpatterns = [

    path('list', FuncionarioList.as_view(), name = 'list_funcionarios'),
    path('create/', FuncionarioNovo.as_view(), name = 'create_funcionarios'),
    path('pdf_reportlab', pdf_reportlab,  name = 'pdf_reportlab'),

    path('relatorio_funcionarios', relatorio_funcionarios, name='relatorio_funcionarios'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
    path('relatorio_funcionarios_html_debug', PdfDebug.as_view(), name='relatorio_funcionarios_html_debug'),

    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionarios'),


]