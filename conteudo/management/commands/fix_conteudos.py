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
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/1_Pensamento%20Computacional/1.png?raw=true",
          modulo="P",
          questao=Questao.objects.get(id=1)
        )

        #2 conteúdo
        Conteudo.objects.create(
          titulo="Algorítimos",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/2_Algoritmo/conteudo1.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=2)
        )

        #3 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas Sequenciais - I",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/conteudo1.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=3)
        )

        #4 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas Sequenciais - II",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/conteudo2.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=4)
        )

        #5 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas Condicionais - I",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/4_Estruturas%20Condicionais/conteudo1.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=5)
        )

        #6 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas Condicionais - II",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/4_Estruturas%20Condicionais/conteudo2.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=6)
        )

        #7 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas Repetição - I",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/5_Estruturas%20Repeticao/conteudo1.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=7)
        )

        #8 conteúdo
        Conteudo.objects.create(
          titulo="Estruturas de Repetição - II",
          url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/5_Estruturas%20Repeticao/conteudo2.png?raw=true",
          modulo="L",
          questao=Questao.objects.get(id=8)
        )