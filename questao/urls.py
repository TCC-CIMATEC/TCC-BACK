from django.urls import path
from .api import QuestaoView

urlpatterns = [
    path('', QuestaoView.as_view(), name="questoes"),
]