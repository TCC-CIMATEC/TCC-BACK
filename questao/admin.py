from django.contrib import admin
from .models import Opcao, Questao

class OpcaoAdmin(admin.ModelAdmin):
  list_display = ('descricao',
                  'correta',)

class QuestaoAdmin(admin.ModelAdmin):
  list_display = ('titulo',
                  'url_img',
                  'opcao1',
                  'opcao2',
                  'opcao3',
                  'opcao4',)



admin.site.register(Opcao, OpcaoAdmin)
admin.site.register(Questao, QuestaoAdmin)