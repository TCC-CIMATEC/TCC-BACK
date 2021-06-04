from django.urls import path
from .api import JogadorView, JogadorRegistrationView, RankingView, JogadorUpdateView

urlpatterns = [
    path('registration/', JogadorRegistrationView.as_view(), name="jogador-create"),
    path('update/', JogadorUpdateView.as_view(), name="jogador-update"),
    path('ranking/', RankingView.as_view(), name="ranking"),
    path('', JogadorView.as_view(), name="jogadores"),
]