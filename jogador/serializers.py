from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Jogador
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class JogadorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Jogador
    fields = ('user', 'pontuacao', 'nivel', )
    allow_null = True
    depth = 2

class JogadorPOSTSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'genero', 'phone', 'categoria', 'password',)


    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    name = serializers.CharField(required=False, max_length=100, allow_blank=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['password'])
        user.phone = validated_data['phone']
        user.genero = validated_data['genero']
        user.categoria = validated_data['categoria']
        user.save()
        if 'name' in validated_data:
            nome_completo = validated_data['name'].split(' ', 1)
            user.first_name = nome_completo[0]
            if len(nome_completo) > 1:
                user.last_name = nome_completo[1]
            user.save()
        else:
            if validated_data['categoria'] == "P":
                return user
            jogador = Jogador.objects.create(
                user=user,
                pontuacao=0, 
                nivel=0
            )
        return user
