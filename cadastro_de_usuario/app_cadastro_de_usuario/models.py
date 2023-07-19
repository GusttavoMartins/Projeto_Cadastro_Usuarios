from django.db import models


class Usuario(models.Model):

    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, null=True)
    cpf = models.TextField(max_length=25, null=True)
    data_nasc = models.DateField(null=True)
    email = models.TextField(max_length=255, null=True)
    telefone = models.IntegerField(null=True)
    genero_choices = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
        ('PND', 'Prefiro não dizer')
    )
    genero = models.CharField(max_length=3, choices=genero_choices, null=True)
