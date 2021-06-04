from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from .models import Turma
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import TurmaSerializer, TurmaPOSTSerializer

class TurmaView(ListCreateAPIView):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class TurmaRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = TurmaPOSTSerializer(data=request.data)
        if serializer.is_valid():
            turma = serializer.save()
            json = serializer.data
            if turma:
                return Response(json, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TurmaUpdateView(RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny, )
    # serializer_class = CustomUserSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        data = request.data
        instance = Turma.objects.filter(id=request.data['id']).first()

        if request.data['id']:
            if not instance:
                return Response({"user": ["Turma não encontrada"]}, status=status.
                                HTTP_400_BAD_REQUEST)
            
            else:
                if 'aluno' in data and (not data['aluno'] == '' or not data['aluno'] == None):
                    instance.alunos.add(data['aluno'])

                instance.save()
                return Response({"message":"Aluno inseridos na turma com sucesso!"}, status=status.HTTP_200_OK)
        
        else:
            return Response({"error": "O parametro id é obrigatório"}, status=status.HTTP_400_BAD_REQUEST)