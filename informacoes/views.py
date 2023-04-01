from django.shortcuts import render, get_list_or_404, redirect
from rest_framework import viewsets, generics
from .serializer import CompromissoSerializer, AgendaSerializer
from .models import Agenda, Compromisso

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset = Compromisso.objects.all()
    serializer_class = CompromissoSerializer