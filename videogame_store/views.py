from rest_framework import viewsets
from .serializer import JogoSerializer, LojaSerializer
from .models import jogo, loja

class JogoViewSet(viewsets.ModelViewSet):
    queryset = jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = loja.objects.all()
    serializer_class = LojaSerializer