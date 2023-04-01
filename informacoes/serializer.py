from rest_framework import serializers
from .models import Agenda, Compromisso

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ['nome', 'telefone', 'email']

class CompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compromisso
        fields = ['data', 'endereco', 'telefone']


