from django.core.management.base import BaseCommand

from conteudo.models import Conteudo
from questao.models import Questao


class Command(BaseCommand):
    help = 'Data da Base Do TCC'

    def handle(self, **options):
        self.stdout.write('Criando Conteúdos')

        #1 conteúdo
        Conteudo.objects.create(
          titulo="Pensamento Computacional",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/1_Pensamento%20Computacional/conteudo1.jpg?raw=true",
          questao=Questao.objects.get(id=1)
        )

        #2 conteúdo
        Conteudo.objects.create(
          titulo="Pensamento Computacional",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/1_Pensamento%20Computacional/conteudo2.jpg?raw=true",
          questao=Questao.objects.get(id=2)
        )

        #3 conteúdo
        Conteudo.objects.create(
          titulo="Algorítimos",
          url_img="",
          questao=Questao.objects.get(id=3)
        )

        #4 conteúdo
        Conteudo.objects.create(
          titulo="Algorítimos",
          url_img="",
          questao=Questao.objects.get(id=4)
        )

        #5 conteúdo
        Conteudo.objects.create(
          titulo="Tipos de Dados",
          url_img="",
          questao=Questao.objects.get(id=5)
        )

        #6 conteúdo
        Conteudo.objects.create(
          titulo="Tipos de Dados",
          url_img="",
          questao=Questao.objects.get(id=6)
        )

        #7 conteúdo
        Conteudo.objects.create(
          titulo="Tipos de Dados",
          url_img="",
          questao=Questao.objects.get(id=7)
        )

        #8 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas Condicionais",
          url_img="",
          questao=Questao.objects.get(id=8)
        )

        #9 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas de Repetição",
          url_img="",
          questao=Questao.objects.get(id=9)
        )