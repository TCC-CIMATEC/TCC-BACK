from django.urls import path
from .api import ConteudoView

urlpatterns = [
    path('', ConteudoView.as_view(), name="conteudo"),
]