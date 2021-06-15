from rest_framework.generics import ListCreateAPIView
from .models import Questao
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import QuestaoSerializer

class QuestaoView(ListCreateAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('id',)