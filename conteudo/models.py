from questao.models import Questao
from django.db import models
from utils.mixins.base import BaseMixin

# Create your models here.
class Conteudo(BaseMixin):
  class Meta:
    verbose_name="Conteúdo"
    verbose_name_plural="Conteúdos"

  MODULO_CHOICES = (
    ('P', u'Pensamento computacional'),
    ('L', u'Lógica de programação'),
  )

  titulo = models.CharField(max_length=150, verbose_name='Título de conteúdo', null=True, blank=True)
  url_img = models.CharField(verbose_name='Imagem do conteúdo', blank=True, max_length=150)
  modulo = models.CharField(max_length=1, blank=True, null=True, choices=MODULO_CHOICES, verbose_name='Módulo')
  questao = models.ForeignKey(Questao, verbose_name='Questão do conteúdo', related_name='Questão', on_delete=models.CASCADE, blank=True, null=True)