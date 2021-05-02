from django.contrib import admin
from .models import Jogador

class JogadorAdmin(admin.ModelAdmin):
  list_display = ('user',
                  'pontuacao', 
                  'faseatualpensamentocomputacional', 
                  'faseatuallogicaprogramacao',)

admin.site.register(Jogador, JogadorAdmin)