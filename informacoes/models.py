from django.db import models

class Agenda(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    data = models.CharField(max_length=100)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=100)
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.data
    
