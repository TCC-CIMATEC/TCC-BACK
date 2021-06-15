from django.core.management.base import BaseCommand

from conteudo.models import Conteudo


class Command(BaseCommand):
    help = 'Data da Base Do TCC'

    def handle(self, **options):
        self.stdout.write('Criando Conteúdos')

        #1 conteúdo
        Conteudo.objects.create(
          titulo="",
          url_img="",
          questao=1
        )