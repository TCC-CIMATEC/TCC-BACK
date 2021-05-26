from django.contrib import admin
from .models import Jogador, FaseLogicaProgramacao, JogadorTurmaFaseLogicaProgramacao

class JogadorAdmin(admin.ModelAdmin):
  list_display = ('user',
                  'pontuacao',
                  'nivel',)

class FaseLogicaProgramacaoAdmin(admin.ModelAdmin):
  list_display = ('categoria',
                  'pontos',
                  'questao',)


class JogadorTurmaFaseLogicaProgramacaoAdmin(admin.ModelAdmin):
  list_display = ('jogador',
                  'fase',)


admin.site.register(Jogador, JogadorAdmin)
admin.site.register(FaseLogicaProgramacao, FaseLogicaProgramacaoAdmin)
admin.site.register(JogadorTurmaFaseLogicaProgramacao, JogadorTurmaFaseLogicaProgramacaoAdmin)