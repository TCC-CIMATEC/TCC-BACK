from django.db import models
from utils.mixins.base import BaseMixin
from questao.models import Questao
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class FaseLogicaProgramacao(BaseMixin):
  class Meta:
    verbose_name="Fase Logica de Programacao"
    verbose_name_plural="Fases Logica de Programacao"

  CATEGORIA_CHOICES = (
        ('O', u'Operadores'),
        ('ES', u'Entrada e Saída de Dados'),
        ('C', u'Condicional'),
        ('R', u'Laço de repetição'),
    )
  
  categoria = models.CharField(max_length=2, blank=True, null=True, choices=CATEGORIA_CHOICES, verbose_name='Categoria da fase')
  pontos = models.IntegerField(verbose_name='Pontos da fase', blank=False, null=False)
  questao = models.OneToOneField(Questao, verbose_name='Questão da fase', on_delete=models.DO_NOTHING, blank=False, null=False)

class FasePensamentoComputacional(BaseMixin):
  class Meta:
    verbose_name="Fase Pensamento Computacional"
    verbose_name_plural="Fases Pensamento Computacional"

  CATEGORIA_CHOICES = (
        ('D', u'Definicao'),
        ('A', u'Algoritimo'),
        ('L', u'Logica'),
    )
  
  categoria = models.CharField(max_length=2, blank=True, null=True, choices=CATEGORIA_CHOICES, verbose_name='Categoria da fase')
  pontos = models.IntegerField(verbose_name='Pontos da fase', blank=False, null=False)
  questao = models.OneToOneField(Questao, verbose_name='Questão da fase', on_delete=models.DO_NOTHING, blank=False, null=False)

class Jogador(BaseMixin):
  class Meta:
    verbose_name="Jogador"
    verbose_name_plural="Jogadores"

  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
  pontuacao = models.IntegerField(verbose_name='Pontuação do jogador', blank=True)
  nivel = models.IntegerField(verbose_name='Nível do jogador', blank=True, null=True)

class JogadorTurmaFaseLogicaProgramacao(BaseMixin):
  class Meta:
    verbose_name="Jogador Turma Fase Logica Programacao"
    verbose_name_plural="Jogadores Turmas Fases Logica Programaca"

  jogador = models.ForeignKey(Jogador, on_delete=models.DO_NOTHING, verbose_name='Jogador')
  fase = models.ForeignKey(FaseLogicaProgramacao, on_delete=models.DO_NOTHING, verbose_name='Fase Lógica Programação')

class JogadorTurmaFasePensamentoComputacional(BaseMixin):
  class Meta:
    verbose_name="Jogador Turma Fase Pensamento Computacional"
    verbose_name_plural="Jogadores Turmas Fases Pensamento Computacional"

  jogador = models.ForeignKey(Jogador, on_delete=models.DO_NOTHING, verbose_name='Jogador')
  fase = models.ForeignKey(FasePensamentoComputacional, on_delete=models.DO_NOTHING, verbose_name='Fase PEnsamento Computacional')