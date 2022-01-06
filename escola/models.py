from django.db import models

class Aluno (models.Model):
    nome = models.CharField (max_length=30)
    rg = models.CharField (max_length=9)
    cpf =models.CharField(max_length=30,verbose_name='cpf')

    def __str__(self):
        return self.nome
