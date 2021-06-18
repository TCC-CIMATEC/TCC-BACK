from django.db import models
from utils.mixins.base import BaseMixin
from questao.models import Questao
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Jogador(BaseMixin):
  class Meta:
    verbose_name="Jogador"
    verbose_name_plural="Jogadores"

  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
  pontuacao = models.IntegerField(verbose_name='Pontuação do jogador', blank=True, default=0)
  nivel = models.IntegerField(verbose_name='Nível do jogador', blank=True, null=True, default=0)
  fasepensamentocomputacional = models.IntegerField(verbose_name='Fase lógica de programação', blank=True, null=True, default=0)
  faselogicaprogramacao = models.IntegerField(verbose_name='Fase lógica de programação', blank=True, null=True, default=0)