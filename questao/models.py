from django.db import models
from utils.mixins.base import BaseMixin

# Create your models here.
class Opcao(BaseMixin):
  class Meta:
    verbose_name="Opção"
    verbose_name_plural="Opções"

  descricao = models.CharField(max_length=150, verbose_name='Descrição da opção', null=True, blank=True)
  correta = models.BooleanField(verbose_name='Opção correta', blank=True)

class Questao(BaseMixin):
  class Meta:
    verbose_name="Questao"
    verbose_name_plural="Questoes"

  titulo = models.CharField(max_length=150, verbose_name='Título da questão')
  url_img = models.CharField(max_length=150, verbose_name='Descrição da questão')
  opcao1 = models.ForeignKey(Opcao, verbose_name='Opção 1', related_name='Opcao1', on_delete=models.CASCADE, blank=True, null=True)
  opcao2 = models.ForeignKey(Opcao, verbose_name='Opção 2', related_name='Opcao2', on_delete=models.CASCADE, blank=True, null=True)
  opcao3 = models.ForeignKey(Opcao, verbose_name='Opção 3', related_name='Opcao3', on_delete=models.CASCADE, blank=True, null=True)
  opcao4 = models.ForeignKey(Opcao, verbose_name='Opção 4', related_name='Opcao4', on_delete=models.CASCADE, blank=True, null=True)