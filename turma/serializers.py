from rest_framework import serializers
from .models import Turma
from django.contrib.auth import get_user_model

User = get_user_model()

class TurmaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Turma
    fields = ('id', 'nome', 'turno', 'professor', 'codigoTurma', 'alunos', )
    allow_null = True
    depth = 2

class TurmaPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = ('id', 'nome', 'turno', 'professor', 'codigoTurma', 'alunos', )

    def create(self, validated_data):
        turma = Turma.objects.create()
        turma.nome = validated_data['nome']
        turma.turno = validated_data['turno']
        turma.professor = validated_data['professor']
        turma.codigoTurma = validated_data['codigoTurma']
        turma.save()
       
        return turma
