# Generated by Django 2.2.9 on 2020-05-18 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0004_auto_20200518_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Classificação da Conta', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(help_text='Descrição da conta', max_length=200)),
                ('vencimento', models.DateField(help_text='Data de Vencimento')),
                ('pagamento', models.DateField(help_text='Data de Pagamento')),
                ('valor', models.DecimalField(decimal_places=2, help_text='Valor', max_digits=12)),
                ('tipo', models.CharField(choices=[('F', 'Fixa'), ('E', 'Eventual')], help_text='Tipo', max_length=1)),
                ('codigo_barras', models.CharField(help_text='Código de Barras', max_length=200)),
                ('classificacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contas.Classificacao')),
                ('pertence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='usuarios.Usuario')),
            ],
        ),
    ]