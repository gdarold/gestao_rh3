"""gestao_rh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import RegistroHoraExtraViewSet
from django.conf.urls.i18n import i18n_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/registro_hora_extra', RegistroHoraExtraViewSet)


urlpatterns = [

    path('admin/', admin.site.urls),


]

urlpatterns += i18n_patterns(
    path('', include('apps.core.urls')),

    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('horas_extras/', include('apps.registro_hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
