from django.core.management.base import BaseCommand

from questao.models import Questao, Opcao


class Command(BaseCommand):
    help = 'Data da Base Do TCC'

    def handle(self, **options):
        self.stdout.write('Criando Questões')

        Opcao.objects.create(
            descricao="a) 3-4-2-1",
            correta=True
        )

        Opcao.objects.create(
            descricao="b) 1 - 2 - 3 -4",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 2 - 1 - 4 - 3",
            correta=False
        )

        Opcao.objects.create(
            descricao="d) 1 - 4 - 2 - 3",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            descricao="Assinale a alternativa correta que representa a sequência de passos correta para a solução do problema atravessar a rua:</br>"
                + "</br>"
                + "Atravessar na faixa de pedestres</br>"
                + "Olhar dos dois lados da rua</br>"
                + "Aguardar o sinal verde da sinalização para pedestres</br>"
                + "Aguardar os carros pararem",
            opcao1=Opcao.objects.get(id=1),
            opcao2=Opcao.objects.get(id=2),
            opcao3=Opcao.objects.get(id=3),
            opcao4=Opcao.objects.get(id=4),
        )
            