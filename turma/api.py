from jogador.models import Jogador
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Turma, User
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import TurmaSerializer

class TurmaView(ListCreateAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id',
                    'professor__id',
                    'alunos__user__id')


class TurmaRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        professor = User.objects.filter(email=request.data['professor']).first()
        if not User:
            return Response({"Turma": ["Professor não encontrado"]}, status=status.
                            HTTP_400_BAD_REQUEST)
        request.data['professor'] = professor
        print(request.data['professor'])

        turma = Turma.objects.create()
        turma.nome = request.data['nome']
        turma.turno = request.data['turno']
        turma.professor = request.data['professor']
        turma.codigoTurma = request.data['codigoTurma']
        turma.save()

        return Response(status=status.HTTP_201_CREATED)

class TurmaUpdateView(RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    # serializer_class = CustomUserSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        data = request.data
        instance = Turma.objects.filter(codigoTurma=request.data['codigoTurma']).first()
        user = User.objects.filter(email=request.data['aluno']).first()
        aluno = Jogador.objects.filter(user=user).first()
        data['aluno'] = aluno

        if request.data['codigoTurma']:
            if not instance:
                return Response({"user": ["Turma não encontrada"]}, status=status.
                                HTTP_400_BAD_REQUEST)
            
            else:
                if 'aluno' in data and (not data['aluno'] == '' or not data['aluno'] == None):
                    instance.alunos.add(data['aluno'])

                instance.save()
                return Response({"message":"Aluno inserido na turma com sucesso!"}, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "O parametro id é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)