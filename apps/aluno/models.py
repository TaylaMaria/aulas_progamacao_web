from django.db import models

# Create your models here.

class Aluno (models.Model):
    nome = models.CharField (max_length=255, null=False, blank=False)
    matricula = models.CharField (max_length=255, null=False, blank=False, unique=True)
    telefone = models.CharField (max_length=20, null=False, blank=False)
    status = models.BooleanField (default=True)

    def __str__ (self):
        return self.nome
