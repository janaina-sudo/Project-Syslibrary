# Syslibrary
O seguinte projeto foi desenvolvido durante a disciplina de banco de dados, trata-se de uma API desenvolvida com Fast API que permite o cadastro de leitores e administradores no sistema de uma biblioteca. Além disso, pode ser realizado o emprestimo de livros para leitores cadastrados no sistema. O administrador, ou empregado, é responsável por gerenciar os emprestimos e livros da biblioteca. 

## Instalação 

```
git clone https://github.com/janaina-sudo/Project-Syslibrary
```

Após o clone do repositório edite as variáveis de ambiente do docker-compose.yml adicionando a senha desejada. Por fim, edite o DATABASE_URL com as configurações de usuário e senhas definidos no serviço do banco.

## Execução do projeto
Para executar com docker digite o comando no terminal do seu ambiente de desenvolvimento:
```
docker-compose up --build

```

