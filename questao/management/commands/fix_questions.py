from django.core.management.base import BaseCommand

from questao.models import Questao, Opcao


class Command(BaseCommand):
    help = 'Data da Base Do TCC'

    def handle(self, **options):
        self.stdout.write('Criando Questões')

        #PENSAMENTO COMPUTACIONAL
        #1 questão
        Opcao.objects.create(
            descricao="a) lógica da programação e como funcionam os algoritmos.",
            correta=True
        )

        Opcao.objects.create(
            descricao="b) a maneira como funcionam os sites e as redes sociais.",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) o manuseio e a função dos aplicativos digitais.",
            correta=False
        )

        Opcao.objects.create(
            descricao="d) o valor dos projetos colaborativos para a globalização.",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://raw.githubusercontent.com/TCC-CIMATEC/questoes-imagens/main/1_Pensamento%20Computacional/questao1.png?raw=true",
            opcao1=Opcao.objects.get(id=1),
            opcao2=Opcao.objects.get(id=2),
            opcao3=Opcao.objects.get(id=3),
            opcao4=Opcao.objects.get(id=4),
        )

        #LÓGICA DE PROGRAMAÇÃO
        #2 questão
        Opcao.objects.create(
            descricao="a)3 - 4 - 2 - 1",
            correta=True
        )

        Opcao.objects.create(
            descricao="b)1 - 2 - 3 -4",
            correta=False
        )

        Opcao.objects.create(
            descricao="c)2 - 1 - 4 - 3",
            correta=False
        )

        Opcao.objects.create(
            descricao="d)1 - 4 - 2 - 3",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/2_Algoritmo/questao1.png?raw=true",
            opcao1=Opcao.objects.get(id=5),
            opcao2=Opcao.objects.get(id=6),
            opcao3=Opcao.objects.get(id=7),
            opcao4=Opcao.objects.get(id=8),
        )


        #ESTRUTURAS SEQUENCIAIS
        #3 questão
        Opcao.objects.create(
            descricao="a) print x;",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) int x;",
            correta=True
        )

        Opcao.objects.create(
            descricao="c) var x;",
            correta=False
        )

        Opcao.objects.create(
            descricao="d) float x;",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/questao1.png?raw=true",
            opcao1=Opcao.objects.get(id=9),
            opcao2=Opcao.objects.get(id=10),
            opcao3=Opcao.objects.get(id=11),
            opcao4=Opcao.objects.get(id=12),
        )

        #ESTRUTURAS SEQUENCIAIS
        #4 questão
        Opcao.objects.create(
            descricao="a) double x;",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) scan x;",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) var x;",
            correta=True
        )

        Opcao.objects.create(
            descricao="d) string x;",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/questao2.png?raw=true",
            opcao1=Opcao.objects.get(id=13),
            opcao2=Opcao.objects.get(id=14),
            opcao3=Opcao.objects.get(id=15),
            opcao4=Opcao.objects.get(id=16),
        )
        
        #ESTRUTURAS CONDICIONAIS
        #5 questão
        Opcao.objects.create(
            descricao="a) 0;",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) 1;",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 2;",
            correta=True
        )

        Opcao.objects.create(
            descricao="d) 3;",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/4_Estruturas%20Condicionais/questao1.png?raw=true",
            opcao1=Opcao.objects.get(id=17),
            opcao2=Opcao.objects.get(id=18),
            opcao3=Opcao.objects.get(id=19),
            opcao4=Opcao.objects.get(id=20),
        )

        #ESTRUTURAS CONDICIONAIS
        #6 questão
        Opcao.objects.create(
            descricao="a) 0;",
            correta=True
        )

        Opcao.objects.create(
            descricao="b) 2;",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 3;",
            correta=False
        )

        Opcao.objects.create(
            descricao="d) 4;",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/4_Estruturas%20Condicionais/questao2.png?raw=true",
            opcao1=Opcao.objects.get(id=21),
            opcao2=Opcao.objects.get(id=22),
            opcao3=Opcao.objects.get(id=23),
            opcao4=Opcao.objects.get(id=24),
        )

        #ESTRUTURAS CONDICIONAIS
        #7 questão
        Opcao.objects.create(
            descricao="a) 0;",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) 1;",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 49;",
            correta=True
        )

        Opcao.objects.create(
            descricao="d) 50;",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/5_Estruturas%20Repeticao/questao1.png?raw=true",
            opcao1=Opcao.objects.get(id=25),
            opcao2=Opcao.objects.get(id=26),
            opcao3=Opcao.objects.get(id=27),
            opcao4=Opcao.objects.get(id=28),
        )

        #ESTRUTURAS CONDICIONAIS
        #8 questão
        Opcao.objects.create(
            descricao="a) 0;",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) 10;",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 19;",
            correta=True
        )

        Opcao.objects.create(
            descricao="d) 20;",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/5_Estruturas%20Repeticao/questao2.png?raw=true",
            opcao1=Opcao.objects.get(id=29),
            opcao2=Opcao.objects.get(id=30),
            opcao3=Opcao.objects.get(id=31),
            opcao4=Opcao.objects.get(id=32),
        )