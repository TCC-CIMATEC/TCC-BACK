# Generated by Django 3.2 on 2021-06-18 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jogador', '0002_auto_20210618_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='faselogicaprogramacao',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Fase lógica de programação'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='fasepensamentocomputacional',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Fase lógica de programação'),
        ),
    ]
