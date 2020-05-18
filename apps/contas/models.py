from django.db import models
from apps.usuarios.models import Usuario


class Classificacao(models.Model):
    descricao = models.CharField(max_length=50, help_text='Classificação da Conta')

    def __str__(self):
        return self.descricao


class Conta(models.Model):
    TIPO_CHOICES = (
        ('F', 'Fixa'),
        ('E', 'Eventual')
    )
    descricao = models.CharField(max_length=200, help_text='Descrição da conta')
    vencimento = models.DateField(help_text='Data de Vencimento')
    pagamento = models.DateField(help_text='Data de Pagamento')
    valor = models.DecimalField(max_digits=12, decimal_places=2, help_text='Valor')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, help_text='Tipo')
    classificacao = models.OneToOneField(Classificacao, on_delete=models.CASCADE, null=False, blank=False)
    codigo_barras = models.CharField(max_length=200, help_text='Código de Barras')
    pertence = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao
