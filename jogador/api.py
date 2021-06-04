from rest_framework import status, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, CreateAPIView
from .models import Jogador
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken
from .serializers import JogadorSerializer, JogadorPOSTSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404  

class RankingView(ListCreateAPIView, CreateAPIView):
    queryset = Jogador.objects.all().order_by('-pontuacao', 'created_at')
    print(queryset)
    serializer_class = JogadorSerializer
    filter_backends = [DjangoFilterBackend]

class JogadorView(ListCreateAPIView, CreateAPIView):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    filter_backends = [DjangoFilterBackend]

class JogadorRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = JogadorPOSTSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokenr = TokenObtainPairSerializer().get_token(user)
            tokena = AccessToken().for_user(user)
            json = serializer.data
            json['refresh'] = str(tokenr)
            json['access'] = str(tokena)
            if user:
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class JogadorUpdateView(RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    # serializer_class = CustomUserSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        data = request.data
        print(request.data['id'])
        instance = Jogador.objects.filter(id=request.data['id']).first()

        if request.data['id']:
            if not instance:
                return Response({"user": ["Usuário não encontrado"]}, status=status.
                                HTTP_400_BAD_REQUEST)
            
            else:
                if 'pontuacao' in data and (not data['pontuacao'] == '' or not data['pontuacao'] == None):
                    instance.pontuacao = data['pontuacao']
                
                if 'nivel' in data and (not data['nivel'] == '' or not data['nivel'] == None):
                    instance.nivel = data['pontuacao']

                instance.save()
                return Response({"message":"Os dados foram atualizados com sucesso!"}, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "O parametro id é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)