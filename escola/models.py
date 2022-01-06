from django.db import models

class Aluno (models.Model):
    nome = models.CharField (max_length=30,null=True)
    rg = models.CharField (max_length=9,null=True)
    
    
    def __str__(self):
        return self.nome
