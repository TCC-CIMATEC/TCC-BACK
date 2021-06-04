from rest_framework.generics import ListCreateAPIView
from .models import Questao
from .serializers import QuestaoSerializer

class QuestaoView(ListCreateAPIView):
    queryset = Questao.objects.all()
    serializer_class = QuestaoSerializer