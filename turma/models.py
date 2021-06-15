from django.db import models
from jogador.models import Jogador
from utils.mixins.base import BaseMixin

from django.contrib.auth import get_user_model

User = get_user_model()

class Turma(BaseMixin):
  class Meta:
    verbose_name="Turma"
    verbose_name_plural="Turmas"

  TURNO_CHOICES = (
      ('M', u'Matutino'),
      ('V', u'Vespertino'),
      ('N', u'Noturno'),
      ('I', u'Integral'),
  )

  nome = models.CharField(max_length=150, verbose_name='Nome da turma', null=True, blank=True)
  turno = models.CharField(max_length=1, blank=True, null=True, choices=TURNO_CHOICES, verbose_name='Turno da turma')
  professor = models.ForeignKey(User, verbose_name='Professor', related_name='Professor', on_delete=models.DO_NOTHING, blank=True, null=True)
  codigoTurma = models.CharField(max_length=30, verbose_name='Código da turma', null=True, blank=True, unique=True)
  alunos = models.ManyToManyField(Jogador, verbose_name='Alunos da turma', related_name='AlunosTurma', blank=True, null=True)