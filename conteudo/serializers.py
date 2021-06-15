from rest_framework import serializers
from .models import Conteudo

class ConteudoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Conteudo
    fields = ('titulo', 'url_img', 'questao',)
    allow_null = True
    depth = 2