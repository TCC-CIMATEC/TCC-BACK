from django.db import models
from utils.mixins.base import BaseMixin
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Jogador(BaseMixin):
  class Meta:
    verbose_name="Jogador"
    verbose_name_plural="Jogadores"

  user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
  pontuacao = models.IntegerField(verbose_name='Pontuação do jogador', blank=True)
  faseatualpensamentocomputacional = models.IntegerField(verbose_name='Fase atual pensamento computacional')
  faseatuallogicaprogramacao = models.IntegerField(verbose_name='Fase atual logica programação')