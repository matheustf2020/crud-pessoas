from django.db import models

class Cargos(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Projetos(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    cargo = models.ForeignKey(Cargos, on_delete=models.DO_NOTHING)
    projetos = models.ManyToManyField(Projetos)

    def __str__(self):
        return self.nome