# Consulta de CNPJ

Este é um projeto de web app para consulta de informações de CNPJ. Ao inserir um número de CNPJ válido, o usuário recebe informações detalhadas sobre a empresa registrada, como razão social, endereço, telefone e situação cadastral. A consulta é feita utilizando a API da ReceitaWS, que fornece dados atualizados sobre o CNPJ consultado.

Você pode acessar o projeto em funcionamento [aqui](https://pedro.pythonanywhere.com/cnpj).

## Funcionalidades

- **Consulta de CNPJ**: o usuário insere um CNPJ e obtém informações detalhadas da empresa.
- **Interface Simples e Intuitiva**: uma interface amigável onde o usuário consegue visualizar os resultados facilmente.
- **Validação de Entrada**: o campo de CNPJ realiza validações para garantir que o formato e o número sejam válidos antes da consulta.
- **Consumo de API Externa**: o sistema utiliza a [API da ReceitaWS](https://receitaws.com.br/) para buscar dados atualizados de empresas.

## Tecnologias Utilizadas

- **Back-end**: Python para gerenciar a lógica de negócios e o consumo da API.
- **Front-end**: HTML e CSS para estrutura e design da página.
- **JavaScript**: para interação e manipulação dinâmica dos dados recebidos da API.
- **API**: ReceitaWS, para consulta dos dados das empresas com base no CNPJ informado.

## Uso

1. Insira o CNPJ no campo de busca e clique em "Consultar".
2. O sistema fará uma requisição para a API da ReceitaWS e exibirá os dados da empresa, incluindo:
   - Nome ou Razão Social
   - Endereço
   - Telefone
   - Situação cadastral
   - Data de abertura, entre outros detalhes.

## Exemplo de Consulta

![Busca_CNPJ](https://github.com/user-attachments/assets/91d08c8d-c356-48e4-a3e4-1958834229e9)

## Estrutura do Projeto

- `cnpj/` - Pasta principal contendo os arquivos Python3 e o APP.
- `config` - Pasta que contém as configurações do Projeto.
- `static/` - Arquivos estáticos como CSS e JavaScript.
- `manage.py` - Arquivo principal do Dajngo que tem como alvo administrar e executar o projeto.
- `README.md` - Instruções e informações sobre o projeto.
