# Generated by Django 2.2.9 on 2020-05-18 04:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20200518_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta',
            name='classificacao',
        ),
        migrations.RemoveField(
            model_name='conta',
            name='pertence',
        ),
        migrations.DeleteModel(
            name='Classificacao',
        ),
        migrations.DeleteModel(
            name='Conta',
        ),
    ]
