from rest_framework import serializers
from .models import jogo, loja

class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = jogo
        fields = ["nome", "preco"]

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = loja
        fields = ["nome", "endereco", "telefone", "telefone_fixo"]