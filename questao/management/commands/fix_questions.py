from django.core.management.base import BaseCommand

from questao.models import Questao, Opcao


class Command(BaseCommand):
    help = 'Data da Base Do TCC'

    def handle(self, **options):
        self.stdout.write('Criando Questões')

        #1 questão
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
            url_img="url imagem",
            opcao1=Opcao.objects.get(id=1),
            opcao2=Opcao.objects.get(id=2),
            opcao3=Opcao.objects.get(id=3),
            opcao4=Opcao.objects.get(id=4),
        )

        #2 questão
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
            titulo="Questão 2",
            url_img="url imagem 2",
            opcao1=Opcao.objects.get(id=5),
            opcao2=Opcao.objects.get(id=6),
            opcao3=Opcao.objects.get(id=7),
            opcao4=Opcao.objects.get(id=8),
        )