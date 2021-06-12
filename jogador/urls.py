from django.urls import path
from django.conf.urls import url
from .api import JogadorView, JogadorRegistrationView, RankingView, JogadorUpdateView, OneUserView

urlpatterns = [
    path('registration/', JogadorRegistrationView.as_view(), name="jogador-create"),
    path('update/', JogadorUpdateView.as_view(), name="jogador-update"),
    path('ranking/', RankingView.as_view(), name="ranking"),
    path('', JogadorView.as_view(), name="jogadores"),
    url(r'^(?P<id>\d+)/$', OneUserView.as_view(), name='jogador'),
]