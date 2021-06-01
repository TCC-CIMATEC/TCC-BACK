from django.contrib import admin
from .models import Turma

class TurmaAdmin(admin.ModelAdmin):
  list_display = ('nome',
                  'turno',
                  'professor',
                  'codigoTurma',
                  'active',)

admin.site.register(Turma, TurmaAdmin)