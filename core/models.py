from django.db import models

#modelo de time
class Time(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

#modelo jogador
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    posicao = models.CharField(max_length=50)
    idade = models.IntegerField()
    #um time pode ter varios jogadores (1,N)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='jogadores')

    def __str__(self):
        return f"{self.nome} ({self.time.nome})"
