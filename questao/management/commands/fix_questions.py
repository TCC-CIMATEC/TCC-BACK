from django.core.management.base import BaseCommand

from questao.models import Questao, Opcao


class Command(BaseCommand):
    help = 'Data da Base Do TCC'

    def handle(self, **options):
        self.stdout.write('Criando Questões')

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
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/1_Pensamento%20Computacional/1.jpg?raw=true",
            opcao1=Opcao.objects.get(id=1),
            opcao2=Opcao.objects.get(id=2),
            opcao3=Opcao.objects.get(id=3),
            opcao4=Opcao.objects.get(id=4),
        )

        #2 questão
        Opcao.objects.create(
            descricao="a)1-A; 2-C; 3-F; 4-D; 5-H; 6-B; 7-G; 8-E; 9-I.",
            correta=False
        )

        Opcao.objects.create(
            descricao="b)1-G; 2-I; 3-E; 4-H; 5-D; 6-C; 7-B; 8-F; 9-A.",
            correta=False
        )

        Opcao.objects.create(
            descricao="c)1-A; 2-I; 3-F; 4-C; 5-D; 6-B; 7-G; 8-E; 9-H.",
            correta=False
        )

        Opcao.objects.create(
            descricao="d)1-B; 2-I; 3-F; 4-H; 5-D; 6-A; 7-G; 8-E; 9-C.",
            correta=True
        )

        Questao.objects.create(
            titulo="Questão 2",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/1_Pensamento%20Computacional/2.jpg?raw=true",
            opcao1=Opcao.objects.get(id=5),
            opcao2=Opcao.objects.get(id=6),
            opcao3=Opcao.objects.get(id=7),
            opcao4=Opcao.objects.get(id=8),
        )

        #3 questão
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
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/2_Algoritmo/1.jpg?raw=true",
            opcao1=Opcao.objects.get(id=9),
            opcao2=Opcao.objects.get(id=10),
            opcao3=Opcao.objects.get(id=11),
            opcao4=Opcao.objects.get(id=12),
        )
        
        #4 questão
        Opcao.objects.create(
            descricao="a) Entrar no carro \n Ajustar Banco e Espelhos \n Colocar cinto de Segurança \n Colocar Carro em ponto morto \n ligar o carro",
            correta=True
        )

        Opcao.objects.create(
            descricao="b)  Entrar no carro \n Ligar o carro",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) Entrar no carro \n Pisar no acelerador",
            correta=False
        )

        Opcao.objects.create(
            descricao="d) Entrar no carro \n Colocar cinto de segurança \n Pisar no acelerador",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 2",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/2_Algoritmo/2.jpg?raw=true",
            opcao1=Opcao.objects.get(id=13),
            opcao2=Opcao.objects.get(id=14),
            opcao3=Opcao.objects.get(id=15),
            opcao4=Opcao.objects.get(id=16),
        )

        #5 questão
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
            descricao="d) float x",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/1.jpg?raw=true",
            opcao1=Opcao.objects.get(id=17),
            opcao2=Opcao.objects.get(id=18),
            opcao3=Opcao.objects.get(id=19),
            opcao4=Opcao.objects.get(id=20),
        )

        #6 questão
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
            correta=False
        )

        Opcao.objects.create(
            descricao="d) string x;",
            correta=True
        )

        Questao.objects.create(
            titulo="Questão 2",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/2.jpg?raw=true",
            opcao1=Opcao.objects.get(id=21),
            opcao2=Opcao.objects.get(id=22),
            opcao3=Opcao.objects.get(id=23),
            opcao4=Opcao.objects.get(id=24),
        )

        #7 questão
        Opcao.objects.create(
            descricao="a) 11",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) 20",
            correta=True
        )

        Opcao.objects.create(
            descricao="c) 19",
            correta=False
        )

        Opcao.objects.create(
            descricao="d) 21",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 3",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/3_Estruturas%20Sequenciais/3.jpg?raw=true",
            opcao1=Opcao.objects.get(id=25),
            opcao2=Opcao.objects.get(id=26),
            opcao3=Opcao.objects.get(id=27),
            opcao4=Opcao.objects.get(id=28),
        )

        #8 questão
        Opcao.objects.create(
            descricao="a) 0",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) 1",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 2",
            correta=True
        )

        Opcao.objects.create(
            descricao="d) 3",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/4_Estruturas%20Condicionais/1_new.jpg?raw=true",
            opcao1=Opcao.objects.get(id=29),
            opcao2=Opcao.objects.get(id=30),
            opcao3=Opcao.objects.get(id=31),
            opcao4=Opcao.objects.get(id=32),
        )

        #9 questão
        Opcao.objects.create(
            descricao="a) 0",
            correta=False
        )

        Opcao.objects.create(
            descricao="b) 1",
            correta=False
        )

        Opcao.objects.create(
            descricao="c) 49",
            correta=True
        )

        Opcao.objects.create(
            descricao="d) 50",
            correta=False
        )

        Questao.objects.create(
            titulo="Questão 1",
            url_img="https://github.com/TCC-CIMATEC/questoes-imagens/blob/main/5_Estruturas%20Repeticao/1_new.jpg?raw=true",
            opcao1=Opcao.objects.get(id=33),
            opcao2=Opcao.objects.get(id=34),
            opcao3=Opcao.objects.get(id=35),
            opcao4=Opcao.objects.get(id=36),
        )