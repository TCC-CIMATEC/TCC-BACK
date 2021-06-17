# Code Wings - Back-end
1. [Endpoints](#endpoints)
    1. [Turmas](#turmas)
    2. [Ranking](#ranking)
    3. [Jogador](#jogador)
2. [Árvore de Arquivos](#árvore-de-arquivos)
3. [Instalação Back-end](#instalação-back-end)
4. [Equipe](#equipe)

## Endpoints

[Endpoints Heroku](https://cimatec-tcc.herokuapp.com/api/)

### Turmas

* GET Turmas: [https://cimatec-tcc.herokuapp.com/api/turma/](https://cimatec-tcc.herokuapp.com/api/turma/)
* Lista todas as turmas e os usuários das turmas

* POST Cadastrar Turma: [https://cimatec-tcc.herokuapp.com/api/turma/registration/](https://cimatec-tcc.herokuapp.com/api/turma/registration/)

```
{
	"nome": "turma de teste",
	"turno": "V",
	"professor": "admin@email.com.br",
	"codigoTurma": "segredo"
}
```

* PUT Cadastrar aluno em uma turma: [https://cimatec-tcc.herokuapp.com/api/turma/add-alunos/](https://cimatec-tcc.herokuapp.com/api/turma/add-alunos/)

```
{
	"codigoTurma": "segredo",
	"aluno": "email-do-aluno@email.com.br"
}
```

### Ranking

* GET Buscar Ranking: [https://cimatec-tcc.herokuapp.com/api/jogador/ranking/](https://cimatec-tcc.herokuapp.com/api/jogador/ranking/)

### Jogador

* GET Buscar Jogadores: [https://cimatec-tcc.herokuapp.com/api/jogador/](https://cimatec-tcc.herokuapp.com/api/jogador/)
* POST Cadastrar Jogador [https://cimatec-tcc.herokuapp.com/api/jogador/registration/](https://cimatec-tcc.herokuapp.com/api/jogador/registration/)

```
{
	"email": "email-do-aluno@email.com.br",
	"password": "12345678",
	"name": "Hudson Duarte",
	"phone": "71998765432",
	"categoria": "A",
	"genero": "M" 
}
```

* POST Autenticar Jogador: [https://cimatec-tcc.herokuapp.com/api/authenticate/token/obtain/](https://cimatec-tcc.herokuapp.com/api/authenticate/token/obtain/)

```
{
	"email": "meu-email@email.com.br",
	"password": "senhanovateste"
}
```

* PUT Alterar Senha Jogador: [https://cimatec-tcc.herokuapp.com/api/authenticate/user/update/](https://cimatec-tcc.herokuapp.com/api/authenticate/user/update/)

```
{
	"email": "meu-email@email.com.br",
	"old_password": "12345678",
	"new_password": "senhanovateste",
	"password_confirmation": "senhanovateste"
}
```

* PUT ALterar Nível de Pontuação do Jogador: [https://cimatec-tcc.herokuapp.com/api/jogador/update/](https://cimatec-tcc.herokuapp.com/api/jogador/update/)

```
{
	"aluno": "email-do-aluno@emial.com.br",
	"nivel": 2,
	"pontuacao": 10
}
```

## Árvore de Arquivos

```
├── TCC-BACK
│   ├──authenticate
|   │   │   ├── management
|   |   │   │   └── commands
|   │   │   ├── migrations
|   │   │   └── tests
│   ├── conteudo
|   │   │   ├── management
|   |   │   │   └── commands
|   │   │   └── migrations
│   ├── jogador
|   │   │   └── migrations
│   ├── node_modules
│   ├── project
│   ├── questao
|   │   │   ├── management
|   |   │   │   └── commands
|   │   │   └── migrations
│   ├── turma
|   │   │   └── migrations
│   ├── utils
|   │   │   └── mixins
```

## Instalação Back-end


## Utilizando virtual enviroment:

### Dependências
1) Python 3
2) Virtual env

### Use os comandos dentro da pasta do projeto:
```bash
virtualenv -p python3  vm
```

```bash
cd project && pip install -r requirements.txt
```

### Rodando o projeto
```bash
fab dev
```

```bash
python manage.py runserver
```

> NOTA: Necessário estar na Virtual env


## Equipe

* [Elisete Vidotti](https://github.com/lizvidotti91)
* [Hudson Duarte](https://github.com/huduarte)
* [João Lucas Andrade](https://github.com/Jlucas93)
* [Jorge Valois](https://github.com/JorgeValois)
* [Luiz Gonzaga](https://github.com/LuizGonzaga91)
