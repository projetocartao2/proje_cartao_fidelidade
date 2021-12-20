from django.db import models

# Create your models here.
class Usuarios(models.Model):
    nome = models.CharField('Nome', max_length=100, null=False, blank=False)
    cpf = models.CharField('Cpf',max_length=11, null=False, blank=False)
    data_nascimento = models.DateField('Data de nascimento',  null=False, blank=False)

    def __str__(self):
        return self.nome
    