from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome do Usuário')
    email = models.EmailField(max_length=100, help_text='Email')
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome


