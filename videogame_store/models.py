from django.db import models

# Create your models here.
class jogo(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.nome

class loja(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=10)
    telefone_fixo = models.CharField(max_length=8)

    def __str__(self):
        return