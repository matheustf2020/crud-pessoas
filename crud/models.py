from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
