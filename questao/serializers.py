from rest_framework import serializers
from .models import Questao

class QuestaoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Questao
    fields = ('titulo', 'url_img', 'opcao1', 'opcao2', 'opcao3', 'opcao4', )
    allow_null = True
    depth = 2