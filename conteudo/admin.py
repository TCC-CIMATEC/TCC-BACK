from django.contrib import admin
from .models import Conteudo


class ConteudoAdmin(admin.ModelAdmin):
  list_display = ('titulo',
                  'url_img',
                  'questao',)

admin.site.register(Conteudo, ConteudoAdmin)