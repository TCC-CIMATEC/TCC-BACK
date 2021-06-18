from django.contrib import admin
from .models import Jogador

class JogadorAdmin(admin.ModelAdmin):
  list_display = ('user',
                  'pontuacao',
                  'nivel',
                  'faselogicaprogramacao',
                  'fasepensamentocomputacional'
                  )


admin.site.register(Jogador, JogadorAdmin)