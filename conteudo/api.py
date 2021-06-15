from rest_framework.generics import ListCreateAPIView
from .models import Conteudo
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ConteudoSerializer

class ConteudoView(ListCreateAPIView):
    queryset = Conteudo.objects.all()
    serializer_class = ConteudoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id',)