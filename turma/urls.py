from django.urls import path
from .api import TurmaView, TurmaRegistrationView, TurmaUpdateView

urlpatterns = [
    path('add-alunos/', TurmaUpdateView.as_view(), name="turma-add"),
    path('registration/', TurmaRegistrationView.as_view(), name="turma-create"),
    path('', TurmaView.as_view(), name="turmas"),
]