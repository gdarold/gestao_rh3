from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import Registro_hora_extraSerializer
from ..models import RegistroHoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = Registro_hora_extraSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)