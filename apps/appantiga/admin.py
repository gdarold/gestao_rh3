from django.contrib import admin
from .models import teste, RegistroUsuarios

# Register your models here.


class RegistroUsuariosAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return RegistroUsuarios.objects.using('antigo').all()


admin.site.register(teste),
admin.site.register(RegistroUsuarios)