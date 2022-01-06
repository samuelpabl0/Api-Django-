from django.db import models

class Aluno (models.Model):
    nome = models.CharField (max_length=30,null=True)
    rg = models.CharField (max_length=9,null=True)
    cpf =models.CharField(max_length=30,verbose_name='cpf',null=true)

    def __str__(self):
        return self.nome
